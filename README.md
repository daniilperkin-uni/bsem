# BSEM — Data Annotation & Dataset Evaluation

University seminar project (B.Sc.) on data-centric AI: how reliable are human annotations,
and how do you evaluate a computer-vision dataset before you train on it?

> **Content warning:** the datasets contain tweets (topics: BLM, Covid-19, Elections 2020)
> with offensive language, slurs and profanity.

## What's in here

| Part | What it does |
|---|---|
| `annotation_experiment/` | Our annotation experiment: 216 tweets, two annotators, discussion, expert adjudication — plus the agreement-metrics work (Bennett's S, Cohen's kappa, Gwet's AC1) and prevalence-paradox simulations |
| `dataset_evaluation/` | A 76-criterion audit of **Microsoft COCO** vs **SA-1B (Segment Anything)** across annotation planning, data sourcing, ethics, quality assurance and adjudication |

## Highlights

**Inter-annotator agreement — discussion closes the gap.** Percentage agreement rises
0.87 → 0.98 and Bennett's S 0.74 → 0.96 between the first pass and the post-discussion labels.

![PA vs Bennett's S](annotation_experiment/figures/fig_agreement_pa_s.png)

**The prevalence paradox.** With rare positives, Cohen's kappa collapses (0.32) while
Bennett's S stays high (0.74) on the very same labels. The simulation notebooks
(`task2_fake_data.ipynb`, `task3_metrics_comparison.ipynb`) show why: kappa is 0 for pure
guessing regardless of prevalence, while S rises with skew — at 5% prevalence, guessing
alone reaches S = 0.81.

**Agreement with the original labels** (n = 216): PA 91.7%, AC1 0.90 against a trivial
"never offensive" baseline of 0.89, kappa 0.50 — so agreement on the rare offensive cases
is only moderate, with a clear topical pattern (BLM missed, Elections 2020 over-labelled).

**Dataset audit:** COCO vs SA-1B on 76 criteria — COCO is the better fit for scene
understanding (semantic categories per object); SA-1B wins on boundary quality (94% of
mask pairs > 90% IoU against professionally corrected masks) but has no categories at all.

## Repository layout

```
annotation_experiment/     our annotation experiment
  annotated_data/          labels + batch metadata (discussion chat logs removed)
  original_data/           original labels used for comparison
  example_data/            small example batches for the exercise notebooks
  figures/                 figures exported by the analysis notebook
  presentation/            result slides (.pptx / .pdf)
  annotated_data_analysis.ipynb   the main analysis
  task1 - task3A*.ipynb    agreement-metric exercises and simulations
dataset_evaluation/        COCO vs SA-1B audit
```

## Run it

```
pip install -r requirements.txt
jupyter lab
```

Open `annotation_experiment/annotated_data_analysis.ipynb` and run all cells — it works
from the repository root or from the folder itself, checks the data with assertions and
writes the figures to `annotation_experiment/figures/`.

## Data & provenance

The tweets, the example batches and the original benchmark labels were provided as part
of the course; the discussion chat logs were removed from the published data files (only
labels, timestamps and batch metadata remain). Paper PDFs are not redistributed — the
evaluation only cites their arXiv IDs.

## Credits & license

Course project by a student group (Group 1); teammates are anonymized. Code: MIT (see
`LICENSE`). Written content and slides: CC BY 4.0. The provided data files are included
for reproducibility without asserting a license on them.
