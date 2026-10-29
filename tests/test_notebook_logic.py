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


if __name__ == "__main__":
    unittest.main()
