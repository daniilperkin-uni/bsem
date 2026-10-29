"""Tests for scripts/validate_data.py.

Every test builds a minimal repository fixture (216 annotated rows, two example
batches, five executed notebooks, four figures, the original labels and a README),
injects exactly one inconsistency and asserts that the validator reports it — so a
regression names the check that stopped working.

Standard library only: ``python -m unittest discover -s tests -v``.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO, "scripts", "validate_data.py")
BATCH_SIZES = [12] + [34] * 6
FIGURES = ("fig_agreement_pa_s.png", "fig_batch_evolution.png",
           "fig_prevalence_by_topic.png", "fig_workflow_overview.png")
HEADER = ["", "text", "final_label"]


def annotated_row(text_id: int, batch: int, text: str | None = None) -> dict:
    """An agreed, undiscussed row — the baseline shape every mutation starts from."""
    return {
        "text_id": text_id,
        "text": text or "[BLM] tweet number %d" % text_id,
        "labels_annotation": [{"user": "anna", "labels": []},
                              {"user": "max", "labels": []}],
        "labels_discussion": [],
        "labels_expert": [],
        "messages_discussion": [],
        "batch_number": batch,
        "batch_annotators": ["anna", "max"],
        "batch_experts": ["expert"],
    }


def build_fixture(root: str) -> None:
    ann = os.path.join(root, "annotation_experiment")
    data = os.path.join(ann, "annotated_data")
    os.makedirs(data)
    text_id = 0
    rows_by_batch = {}
    for batch, size in enumerate(BATCH_SIZES, 1):
        rows = []
        for _ in range(size):
            text_id += 1
            rows.append(annotated_row(text_id, batch))
        rows_by_batch[batch] = rows
    # One row whose discussion did not settle it (expert decides), one that it did.
    disputed = rows_by_batch[1][0]
    disputed["labels_annotation"] = [{"user": "anna", "labels": []},
                                     {"user": "max", "labels": ["Offensiveness"]}]
    disputed["labels_discussion"] = [{"user": "anna", "labels": []},
                                     {"user": "max", "labels": ["Offensiveness"]}]
    disputed["labels_expert"] = [{"user": "expert", "labels": ["Offensiveness"]}]
    settled = rows_by_batch[1][1]
    settled["labels_annotation"] = [{"user": "anna", "labels": []},
                                    {"user": "max", "labels": ["Offensiveness"]}]
    settled["labels_discussion"] = [{"user": "anna", "labels": []},
                                    {"user": "max", "labels": []}]
    for batch, rows in rows_by_batch.items():
        with open(os.path.join(data, "batch_%d.jsonl" % batch), "w", encoding="utf-8") as fh:
            fh.writelines(json.dumps(row) + "\n" for row in rows)

    example = os.path.join(ann, "example_data")
    os.makedirs(example)
    for name in ("batch_14.jsonl", "batch_43.jsonl"):
        with open(os.path.join(example, name), "w", encoding="utf-8") as fh:
            fh.write(json.dumps(annotated_row(1, 14)) + "\n")

    original = os.path.join(ann, "original_data")
    os.makedirs(original)
    with open(os.path.join(original, "original_final_labels.csv"), "w", encoding="utf-8") as fh:
        fh.write(",".join(HEADER) + "\n")
        for row in (r for rows in rows_by_batch.values() for r in rows):
            fh.write("0,%s,0\n" % row["text"])

    for name in ("annotated_data_analysis", "task1_analysis", "task2_fake_data",
                 "task3_metrics_comparison", "task3A_example_prevalence"):
        notebook = {"cells": [{"cell_type": "code", "execution_count": 1, "outputs": [],
                               "source": ["1 + 1"], "metadata": {}}],
                    "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
        with open(os.path.join(ann, name + ".ipynb"), "w", encoding="utf-8") as fh:
            json.dump(notebook, fh)

    figures = os.path.join(ann, "figures")
    os.makedirs(figures)
    for figure in FIGURES:
        with open(os.path.join(figures, figure), "wb") as fh:
            fh.write(b"\x89PNG\r\n\x1a\n")

    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("# fixture\n\nNo images here.\n")


def run_validator(root: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, SCRIPT, "--root", root],
                          capture_output=True, text=True)


class ValidatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="bsem-validator-")
        cls.base = os.path.join(cls.tmp, "fixture")
        build_fixture(cls.base)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def copy(self) -> str:
        target = os.path.join(self.tmp, self.id().rsplit(".", 1)[-1])
        shutil.copytree(self.base, target)
        return target

    def batch_path(self, root: str, batch: int = 1) -> str:
        return os.path.join(root, "annotation_experiment", "annotated_data", "batch_%d.jsonl" % batch)

    def read_rows(self, root: str, batch: int = 1) -> list[dict]:
        with open(self.batch_path(root, batch), encoding="utf-8") as fh:
            return [json.loads(line) for line in fh if line.strip()]

    def write_rows(self, root: str, rows: list[dict], batch: int = 1) -> None:
        with open(self.batch_path(root, batch), "w", encoding="utf-8") as fh:
            fh.writelines(json.dumps(row) + "\n" for row in rows)

    def assert_rejected(self, root: str, message: str) -> None:
        result = run_validator(root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)

    def test_repository_data_passes(self):
        result = run_validator(REPO)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK: 7 batch files, 216 rows, 0 errors", result.stdout)

    def test_fixture_passes(self):
        result = run_validator(self.base)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_text_id_rejected(self):
        root = self.copy()
        rows = self.read_rows(root)
        rows[1]["text_id"] = rows[0]["text_id"]
        self.write_rows(root, rows)
        self.assert_rejected(root, "duplicate text_id")

    def test_duplicate_text_rejected(self):
        root = self.copy()
        rows = self.read_rows(root)
        rows[1]["text"] = rows[0]["text"]
        self.write_rows(root, rows)
        self.assert_rejected(root, "duplicate text (first seen at")

    def test_missing_annotator_rejected(self):
        root = self.copy()
        rows = self.read_rows(root)
        rows[2]["labels_annotation"] = rows[2]["labels_annotation"][:1]
        self.write_rows(root, rows)
        self.assert_rejected(root, "do not match batch_annotators")

    def test_expert_not_declared_rejected(self):
        root = self.copy()
        rows = self.read_rows(root)
        rows[0]["labels_expert"] = [{"user": "stranger", "labels": ["Offensiveness"]}]
        self.write_rows(root, rows)
        self.assert_rejected(root, "not declared in batch_experts")

    def test_expert_label_on_settled_row_rejected(self):
        root = self.copy()
        rows = self.read_rows(root)
        rows[1]["labels_expert"] = [{"user": "expert", "labels": ["Offensiveness"]}]
        self.write_rows(root, rows)
        self.assert_rejected(root, "labels_expert is present but the labels after the discussion agree")

    def test_missing_expert_label_on_unsettled_row_rejected(self):
        root = self.copy()
        rows = self.read_rows(root)
        rows[0]["labels_expert"] = []
        self.write_rows(root, rows)
        self.assert_rejected(root, "labels_expert is empty but the labels after the discussion still disagree")

    def test_example_data_invalid_json_rejected(self):
        root = self.copy()
        with open(os.path.join(root, "annotation_experiment", "example_data", "batch_14.jsonl"),
                  "a", encoding="utf-8") as fh:
            fh.write("{not json}\n")
        self.assert_rejected(root, "example_data/batch_14.jsonl:2: invalid JSON")

    def test_example_data_missing_key_rejected(self):
        root = self.copy()
        path = os.path.join(root, "annotation_experiment", "example_data", "batch_43.jsonl")
        row = annotated_row(1, 43)
        del row["labels_expert"]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
        self.assert_rejected(root, "missing keys ['labels_expert']")

    def test_example_data_annotator_mismatch_rejected(self):
        root = self.copy()
        path = os.path.join(root, "annotation_experiment", "example_data", "batch_43.jsonl")
        row = annotated_row(1, 43)
        row["labels_annotation"] = row["labels_annotation"][:1]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
        self.assert_rejected(root, "example_data/batch_43.jsonl:1: labels_annotation users")

    def test_original_labels_duplicate_text_rejected(self):
        root = self.copy()
        path = os.path.join(root, "annotation_experiment", "original_data",
                            "original_final_labels.csv")
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        lines[-1] = "0,%s,0" % lines[-2].split(",")[1]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        self.assert_rejected(root, "original_final_labels.csv:217: duplicate text")

    def test_original_labels_without_text_column_rejected(self):
        root = self.copy()
        path = os.path.join(root, "annotation_experiment", "original_data",
                            "original_final_labels.csv")
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        lines[0] = ",tweet,final_label"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        self.assert_rejected(root, "no text column")

    def test_unexecuted_notebook_cell_rejected(self):
        root = self.copy()
        path = os.path.join(root, "annotation_experiment", "task1_analysis.ipynb")
        with open(path, encoding="utf-8") as fh:
            notebook = json.load(fh)
        notebook["cells"][0]["execution_count"] = None
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(notebook, fh)
        self.assert_rejected(root, "unexecuted cells")


if __name__ == "__main__":
    unittest.main()
