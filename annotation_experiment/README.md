# Annotation Experiment – Group 1

Offensiveness annotation of 216 tweets (BLM, Covid-19, Elections2020) in 7 batches with Arbiter.
Two annotators label every tweet; disagreements are discussed; disagreements that remain go to the expert.

## Contents

| Path | What it is |
|---|---|
| `annotated_data/batch_1–7.jsonl` | Arbiter export: annotations, discussion labels and messages, expert labels |
| `annotated_data/codebook_initial.md` | Codebook as assigned to us (the course platform) |
| `annotated_data/codebook.md` | Final codebook after our revisions |
| `original_data/original_final_labels.csv` | Original final labels for comparison |
| `annotated_data_analysis.ipynb` | **Analysis** – all results |
| `figures/` | Figures exported by the notebook |
| `presentation/presentation_annotation_experiment.pptx` | Result slides (editable) |
| `presentation/presentation_annotation_experiment.pdf` | Result slides, exported from the .pptx |
| `task*.ipynb`, `example_analysis.ipynb`, `example_data/` | Warm-up exercises on example and fake data (Day 3), not part of this analysis |

## Run

All results come from **`annotated_data_analysis.ipynb`**: open it and run all cells.
It needs Python 3 with `numpy`, `pandas` and `matplotlib`, works from `annotation_experiment/` or the repo root,
checks the data with assertions and writes the figures to `figures/`.

The exercise notebooks (`task*.ipynb`, `example_analysis.ipynb`) are not needed for the results;
`example_analysis.ipynb` additionally requires the course package `arbiter_analysis`.
