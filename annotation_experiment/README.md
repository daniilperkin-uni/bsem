# Annotation Experiment — Group 1

Offensiveness annotation of 216 tweets (BLM, Covid-19, Elections2020) in 7 batches with Arbiter.
Two annotators label every tweet; disagreements are discussed; disagreements that remain go to the expert.

## Contents

| Path | What it is |
|---|---|
| `annotated_data/batch_1-7.jsonl` | Annotation export: labels before/after discussion and expert labels, batch metadata (discussion chat logs removed) |
| `annotated_data/codebook.md` | Our final codebook |
| `original_data/original_final_labels.csv` | Original labels of the source data, for comparison |
| `annotated_data_analysis.ipynb` | **Analysis** — all results |
| `figures/` | Figures exported by the notebook |
| `presentation/presentation_annotation_experiment.pptx` | Result slides (editable) |
| `presentation/presentation_annotation_experiment.pdf` | Result slides, exported from the .pptx |
| `task*.ipynb`, `example_data/` | Warm-up exercises on example and fake data (agreement metrics across prevalences) |

## Run

All results come from **`annotated_data_analysis.ipynb`**: open it and run all cells.
It needs Python 3 with `numpy`, `pandas` and `matplotlib`, works from `annotation_experiment/` or the repo root,
checks the data with assertions and writes the figures to `figures/`.
