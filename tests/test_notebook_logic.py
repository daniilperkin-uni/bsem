"""Tests for the analysis code that lives inside the notebooks.

The helpers are defined in notebook cells and are not importable, so each test loads the
shipped cell source, keeps only the requested function definitions and executes those.
Nothing else from the notebook runs — no file I/O, no plotting, no state.

Needs ``pandas``/``numpy`` from requirements.txt: ``python -m unittest discover -s tests -v``.
"""
from __future__ import annotations

import ast
import json
import os
import unittest
import warnings

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS = os.path.join(REPO, "annotation_experiment")


def functions(notebook: str, *names: str) -> dict:
    """Execute only the named function definitions from a notebook's code cells."""
    with open(os.path.join(NOTEBOOKS, notebook), encoding="utf-8") as fh:
        cells = json.load(fh)["cells"]
    source = "\n".join("".join(cell["source"]) for cell in cells if cell["cell_type"] == "code")
    tree = ast.parse(source)
    wanted: list[ast.stmt] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            wanted.append(node)
    missing = set(names) - {node.name for node in wanted if isinstance(node, ast.FunctionDef)}
    if missing:
        raise AssertionError("function(s) %s not found in %s" % (sorted(missing), notebook))
    namespace: dict = {"np": np, "pd": pd}
    exec(compile(ast.Module(body=wanted, type_ignores=[]), notebook, "exec"), namespace)
    return namespace


class Task1MetricsTest(unittest.TestCase):
    """QA-001: a sample nobody labelled must not count as an agreement."""

    @classmethod
    def setUpClass(cls):
        cls.ns = functions("task1_analysis.ipynb", "get_user_label", "compute_metrics")

    def frame(self, rows):
        df = pd.DataFrame({"labels_annotation": rows})
        df["anna"] = df["labels_annotation"].apply(lambda labels: self.ns["get_user_label"](labels, "anna"))
        df["max"] = df["labels_annotation"].apply(lambda labels: self.ns["get_user_label"](labels, "max"))
        return df

    def test_unlabelled_sample_returns_no_label(self):
        self.assertIsNone(self.ns["get_user_label"]([], "anna"))
        self.assertIsNone(self.ns["get_user_label"]([{"user": "max", "labels": []}], "anna"))

    def test_label_extraction(self):
        get_user_label = self.ns["get_user_label"]
        self.assertEqual(get_user_label([{"user": "anna", "labels": ["offensive"]}], "anna"),
                         "offensive")
        self.assertEqual(get_user_label([{"user": "anna", "labels": []}], "anna"),
                         "not offensive")

    def test_two_missing_labels_are_not_an_agreement(self):
        metrics = self.ns["compute_metrics"](self.frame([[]]))
        self.assertEqual(metrics["Agreements"], 0)
        self.assertTrue(np.isnan(metrics["po_val"]))

    def test_agreement_uses_complete_pairs_only(self):
        rows = [[{"user": "anna", "labels": ["offensive"]},
                 {"user": "max", "labels": ["offensive"]}],
                [{"user": "anna", "labels": []}, {"user": "max", "labels": []}],
                []]
        metrics = self.ns["compute_metrics"](self.frame(rows))
        self.assertEqual(metrics["N"], 2)
        self.assertEqual(metrics["Agreements"], 2)
        self.assertEqual(metrics["po_val"], 1.0)
        self.assertEqual(metrics["s_val"], 1.0)


class Task3APrevalenceTest(unittest.TestCase):
    """QA-001 in the topic notebook: same sentinel, same fix."""

    @classmethod
    def setUpClass(cls):
        cls.ns = functions("task3A_example_prevalence.ipynb", "get_label", "evaluate_group")

    def frame(self, rows):
        df = pd.DataFrame({"labels_annotation": rows})
        df["anna"] = df["labels_annotation"].apply(lambda labels: self.ns["get_label"](labels, "anna"))
        df["max"] = df["labels_annotation"].apply(lambda labels: self.ns["get_label"](labels, "max"))
        return df

    def test_unlabelled_sample_returns_no_label(self):
        self.assertIsNone(self.ns["get_label"]([], "anna"))

    def test_incomplete_samples_are_dropped(self):
        rows = [[{"user": "anna", "labels": ["offensive"]},
                 {"user": "max", "labels": ["offensive"]}],
                [{"user": "anna", "labels": []},
                 {"user": "max", "labels": ["offensive"]}],
                []]
        result = self.ns["evaluate_group"](self.frame(rows), "Test")
        self.assertEqual(result["Total (N)"], 2)
        self.assertEqual(result["Agreements"], 1)
        self.assertEqual(result["prevalence_num"], 1.0)


class Task3DiscussionTest(unittest.TestCase):
    """QA-002: an annotator without a discussion entry keeps the first-pass label."""

    @classmethod
    def setUpClass(cls):
        # staticmethod: a plain function on the class would bind self as the first argument
        cls.offensive = staticmethod(functions("task3_metrics_comparison.ipynb", "offensive")["offensive"])

    def row(self, discussion):
        return pd.Series({
            "text_id": 1,
            "labels_annotation": [{"user": "anna", "labels": []},
                                  {"user": "max", "labels": ["offensive"]}],
            "labels_discussion": discussion,
        })

    def test_annotator_missing_from_the_discussion_keeps_their_label(self):
        row = self.row([{"user": "anna", "labels": ["offensive"]}])
        self.assertFalse(self.offensive(row, "anna", "before"))
        self.assertTrue(self.offensive(row, "max", "before"))
        self.assertTrue(self.offensive(row, "max", "after"))

    def test_recorded_discussion_label_wins(self):
        row = self.row([{"user": "anna", "labels": ["offensive"]},
                        {"user": "max", "labels": []}])
        self.assertTrue(self.offensive(row, "anna", "after"))
        self.assertFalse(self.offensive(row, "max", "after"))

    def test_undiscussed_row_keeps_the_first_pass(self):
        row = self.row([])
        self.assertFalse(self.offensive(row, "anna", "after"))
        self.assertTrue(self.offensive(row, "max", "after"))


class AgreementGuardTest(unittest.TestCase):
    """QA-003: a unanimous slice has no defined chance-corrected agreement."""

    @classmethod
    def setUpClass(cls):
        # staticmethod: a plain function on the class would bind self as the first argument
        cls.main = staticmethod(functions("annotated_data_analysis.ipynb", "agreement")["agreement"])
        cls.task3 = staticmethod(functions("task3_metrics_comparison.ipynb", "agreement")["agreement"])

    def test_unanimous_slice_returns_nan_without_warning(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            result = self.main(np.zeros(20), np.zeros(20))
        self.assertEqual(result["PA"], 1.0)
        self.assertEqual(result["S"], 1.0)
        self.assertTrue(np.isnan(result["kappa"]))

    def test_task3_agreement_guards_kappa_too(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            result = self.task3(np.ones(10, dtype=bool), np.ones(10, dtype=bool))
        self.assertEqual(result["PA"], 1.0)
        self.assertTrue(np.isnan(result["Cohen's κ"]))

    def test_regular_slice_is_unchanged(self):
        a = np.array([0, 1, 1, 0])
        b = np.array([0, 1, 0, 0])
        result = self.main(a, b)
        self.assertAlmostEqual(result["PA"], 0.75)
        self.assertAlmostEqual(result["S"], 0.5)
        self.assertAlmostEqual(result["kappa"], 0.5)
        self.assertAlmostEqual(result["AC1"], 0.5294117647058824)


if __name__ == "__main__":
    unittest.main()
