#!/usr/bin/env python3
"""Validate the published data, notebooks and figures of this repository.

Standard library only — used by CI (.github/workflows/validate.yml).

Beyond shape and row counts, the annotated batches are checked against the
invariants the analysis notebook relies on but never re-checks in CI:

* ``text_id`` is unique across all batches — it is the per-sample identifier
  the plots and the per-row lookup use;
* ``text`` is unique in the batches *and* in ``original_final_labels.csv`` —
  the analysis joins the two on ``text`` with ``validate="one_to_one"``, so a
  duplicate on either side aborts the notebook with a ``MergeError``;
* each row carries exactly one ``labels_annotation`` entry per annotator
  declared in ``batch_annotators`` — a missing entry would silently drop that
  annotator from the agreement statistics;
* ``labels_discussion`` is non-empty exactly when the first-pass labels
  disagreed — a discussion round only happens after a disagreement, so a
  discussion on an agreed row (or none on a disagreed row) means the export
  is inconsistent;
* ``labels_expert`` carries entries only for experts declared in
  ``batch_experts``, and only on the rows that still disagreed after the
  discussion — the analysis asserts exactly that before it builds the final
  label;
* ``text`` contains no URL and no ``@mention`` — the public repo promises
  neither is published;
* ``example_data/*.jsonl`` parses as JSONL and has the same keys and
  annotators as the annotated batches — the exercise notebooks load those
  files without any check of their own.

All errors are reported, not just the first one per file, and every message
carries the file name and the line number, so one CI run lists everything.
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
URL_RE = re.compile(r"https?://|www\.", re.IGNORECASE)
MENTION_RE = re.compile(r"@[A-Za-z0-9_]")


def excerpt(text: str, start: int, end: int, context: int = 20) -> str:
    """Return the matched span with a little context, for error messages."""
    return text[max(0, start - context):min(len(text), end + context)].strip()


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
    seen_ids: dict[object, str] = {}
    seen_texts: dict[str, str] = {}
    for name in batches:
        with open(os.path.join(data, name), encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                where = "%s:%d" % (name, lineno)
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append("%s: invalid JSON (%s)" % (where, exc))
                    continue
                total += 1

                missing = BATCH_KEYS - set(row)
                if missing:
                    errors.append("%s: missing keys %s" % (where, sorted(missing)))
                    continue  # the remaining checks need the full row

                text_id = row["text_id"]
                if text_id in seen_ids:
                    errors.append("%s: duplicate text_id %r (first seen at %s)"
                                  % (where, text_id, seen_ids[text_id]))
                else:
                    seen_ids[text_id] = where

                text = row["text"] or ""
                if text in seen_texts:
                    errors.append("%s: duplicate text (first seen at %s); the analysis joins on "
                                  "text with validate=\"one_to_one\"" % (where, seen_texts[text]))
                else:
                    seen_texts[text] = where

                check(not row["messages_discussion"],
                      "%s: discussion messages were not stripped" % where)
                # Arbiter stores the label name in non-empty lists; [] = not offensive.
                bad = ["%s=%s" % (field, value)
                       for field in ("labels_annotation", "labels_discussion", "labels_expert")
                       for entry in (row[field] or []) for value in (entry.get("labels") or [])
                       if value != "Offensiveness"]
                check(not bad, "%s: unexpected label values %s" % (where, bad))

                declared = row["batch_annotators"] or []
                users = [entry.get("user") for entry in (row["labels_annotation"] or [])]
                check(sorted(users) == sorted(declared),
                      "%s: labels_annotation users %s do not match batch_annotators %s"
                      % (where, users, declared))

                first_pass: dict[object, tuple[str, ...]] = {}
                for entry in (row["labels_annotation"] or []):
                    first_pass.setdefault(entry.get("user"),
                                          tuple(sorted(entry.get("labels") or [])))
                disagreed = len(set(first_pass.values())) > 1
                discussed = bool(row["labels_discussion"])
                check(disagreed == discussed,
                      "%s: labels_discussion is %s but the first pass %s (%s)"
                      % (where, "non-empty" if discussed else "empty",
                         "disagreed" if disagreed else "agreed",
                         ", ".join("%s=%s" % (user, list(labels))
                                   for user, labels in first_pass.items())))

                experts = row["batch_experts"] or []
                expert_users = [entry.get("user") for entry in (row["labels_expert"] or [])]
                check(set(expert_users) <= set(experts),
                      "%s: labels_expert users %s are not declared in batch_experts %s"
                      % (where, expert_users, experts))
                # The final label is the expert's when the discussion did not settle the row.
                after = dict(first_pass)
                for entry in (row["labels_discussion"] or []):
                    after[entry.get("user")] = tuple(sorted(entry.get("labels") or []))
                settled = len(set(after.values())) == 1
                check(bool(expert_users) == (not settled),
                      "%s: labels_expert is %s but the labels after the discussion %s (%s)"
                      % (where, "present" if expert_users else "empty",
                         "agree" if settled else "still disagree",
                         ", ".join("%s=%s" % (user, list(labels))
                                   for user, labels in after.items())))

                url = URL_RE.search(text)
                if url:
                    errors.append("%s: text contains a URL: %r"
                                  % (where, excerpt(text, url.start(), url.end())))
                mention = MENTION_RE.search(text)
                if mention:
                    errors.append("%s: text contains an @mention: %r"
                                  % (where, excerpt(text, mention.start(), mention.end())))
    check(total == N_ROWS, "expected %d annotated rows, found %d" % (N_ROWS, total))

    example = os.path.join(ann, "example_data")
    examples = sorted(f for f in os.listdir(example) if f.endswith(".jsonl"))
    check(len(examples) >= 2, "example_data: expected at least 2 files, found %d" % len(examples))
    for name in examples:
        seen_rows = 0
        with open(os.path.join(example, name), encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                seen_rows += 1
                where = "example_data/%s:%d" % (name, lineno)
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append("%s: invalid JSON (%s)" % (where, exc))
                    continue
                missing = BATCH_KEYS - set(row)
                if missing:
                    errors.append("%s: missing keys %s" % (where, sorted(missing)))
                    continue
                declared = row["batch_annotators"] or []
                users = [entry.get("user") for entry in (row["labels_annotation"] or [])]
                check(sorted(users) == sorted(declared),
                      "%s: labels_annotation users %s do not match batch_annotators %s"
                      % (where, users, declared))
        check(seen_rows > 0, "example_data/%s is empty" % name)

    with open(os.path.join(ann, "original_data", "original_final_labels.csv"), encoding="utf-8") as fh:
        original = list(csv.reader(fh))
    check(len(original) - 1 == N_ROWS, "original_final_labels.csv: expected %d rows" % N_ROWS)
    header, body = original[0], original[1:]
    if "text" not in header:
        errors.append("original_final_labels.csv: no text column — the analysis joins on it")
    else:
        column = header.index("text")
        seen_original: dict[str, int] = {}
        for lineno, values in enumerate(body, 2):
            if len(values) <= column:
                continue
            if values[column] in seen_original:
                errors.append("original_final_labels.csv:%d: duplicate text (first seen at line %d)"
                              % (lineno, seen_original[values[column]]))
            else:
                seen_original[values[column]] = lineno

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

    summary = "%d batch files, %d rows, %d errors" % (len(batches), total, len(errors))
    if errors:
        print("FAIL")
        for error in errors:
            print(" -", error)
        print("FAIL: %s" % summary)
        return 1
    print("OK: %s; %d example files, %d original labels, %d executed notebooks, %d figures"
          % (summary, len(examples), N_ROWS, len(notebooks), len(FIGURES)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
