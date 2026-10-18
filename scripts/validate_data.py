#!/usr/bin/env python3
"""Validate the published data, notebooks and figures of this repository.

Standard library only — used by CI (.github/workflows/validate.yml).
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys

BATCH_KEYS = {"text_id", "text", "labels_annotation", "labels_discussion",
              "labels_expert", "messages_discussion", "batch_number",
              "batch_annotators", "batch_experts"}
FIGURES = ("fig_agreement_pa_s.png", "fig_batch_evolution.png",
           "fig_prevalence_by_topic.png", "fig_workflow_overview.png")
N_BATCHES, N_ROWS, N_NOTEBOOKS = 7, 216, 5


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    root = parser.parse_args().root
    errors: list[str] = []

    def check(ok: bool, message: str) -> None:
        if not ok:
            errors.append(message)

    ann = os.path.join(root, "annotation_experiment")
    data = os.path.join(ann, "annotated_data")
    batches = sorted(f for f in os.listdir(data) if re.fullmatch(r"batch_\d+\.jsonl", f))
    check(len(batches) == N_BATCHES, "expected %d batch files, found %d" % (N_BATCHES, len(batches)))

    total = 0
    for name in batches:
        with open(os.path.join(data, name), encoding="utf-8") as fh:
            rows = [json.loads(line) for line in fh if line.strip()]
        total += len(rows)
        for row in rows:
            missing = BATCH_KEYS - set(row)
            if missing:
                errors.append("%s: missing keys %s" % (name, sorted(missing)))
                break
            if row["messages_discussion"]:
                errors.append("%s: discussion messages were not stripped" % name)
                break
            # Arbiter stores the label name in non-empty lists; [] = not offensive.
            bad = [v for field in ("labels_annotation", "labels_discussion", "labels_expert")
                   for entry in row[field] for v in entry.get("labels", [])
                   if v != "Offensiveness"]
            if bad:
                errors.append("%s: unexpected label values %s" % (name, bad))
                break
    check(total == N_ROWS, "expected %d annotated rows, found %d" % (N_ROWS, total))

    example = os.path.join(ann, "example_data")
    examples = sorted(f for f in os.listdir(example) if f.endswith(".jsonl"))
    check(len(examples) >= 2, "example_data: expected at least 2 files, found %d" % len(examples))
    for name in examples:
        with open(os.path.join(example, name), encoding="utf-8") as fh:
            check(any(line.strip() for line in fh), "example_data/%s is empty" % name)

    with open(os.path.join(ann, "original_data", "original_final_labels.csv"), encoding="utf-8") as fh:
        check(len(list(csv.reader(fh))) - 1 == N_ROWS,
              "original_final_labels.csv: expected %d rows" % N_ROWS)

    notebooks = sorted(f for f in os.listdir(ann) if f.endswith(".ipynb"))
    check(len(notebooks) == N_NOTEBOOKS, "expected %d notebooks, found %d" % (N_NOTEBOOKS, len(notebooks)))
    for name in notebooks:
        with open(os.path.join(ann, name), encoding="utf-8") as fh:
            nb = json.load(fh)
        code = [c for c in nb["cells"] if c["cell_type"] == "code"]
        check(all(c.get("execution_count") for c in code), "%s: unexecuted cells" % name)
        check(not [o for c in code for o in c.get("outputs", []) if o.get("output_type") == "error"],
              "%s: error outputs present" % name)

    figures = os.path.join(ann, "figures")
    for figure in FIGURES:
        check(os.path.exists(os.path.join(figures, figure)), "missing figure %s" % figure)

    with open(os.path.join(root, "README.md"), encoding="utf-8") as fh:
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", fh.read()):
            if not target.startswith("http"):
                check(os.path.exists(os.path.join(root, target)), "README image missing: %s" % target)

    if errors:
        print("FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("OK: %d batches / %d rows, %d example files, %d original labels, "
          "%d executed notebooks, %d figures" % (len(batches), total, len(examples),
                                                 N_ROWS, len(notebooks), len(FIGURES)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
