# Dataset Evaluation


## Group Discussion

| Criterion                          | Guiding Question                                                                                                   | Source           | Dataset 1 | Dataset 2 | Dataset 3 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- | --------- | --------- | --------- |
| Data Correctness & Quality Control | Are the data correct and fact-checked, and were attention checks used to ensure worker diligence?                  | group discussion |           |           |           |
| Content Safety & Moderation        | Is the dataset screened and free of disturbing, toxic, or offensive content?                                       | group discussion |           |           |           |
| Task Specificity                   | Are the data instances sufficiently specific, well-scoped, and tailored to the target task?                        | group discussion |           |           |           |
| Annotation Reliability             | Are the annotations reliable and internally consistent (e.g., measured via inter-annotator agreement metrics)?     | group discussion |           |           |           |
| Provenance & Source Credibility    | Where do the data originate, is the source credible, and is the collection lineage fully documented?               | group discussion |           |           |           |
| Labor Ethics & Working Conditions  | Were crowdworkers or outsourced annotators compensated fairly and provided ethical working conditions?             | group discussion |           |           |           |
| Privacy & Regulatory Compliance    | Does the dataset adhere to privacy regulations (e.g., GDPR) and exclude personally identifiable information (PII)? | group discussion |           |           |           |
| Representativeness & Objectivity   | Is the sample representative and objective, minimizing demographic, geographic, or sampling bias?                  | group discussion |           |           |           |
| Temporal Currency                  | Are the data up to date and temporally valid for time-sensitive domains (e.g., statutes, medical facts, news)?     | group discussion |           |           |           |
| Contextual Completeness            | Are the records complete, and is adequate context preserved to interpret each instance accurately?                 | group discussion |           |           |           |
| Annotator Background & Expertise   | What is the background of the data workers, and do they possess the necessary domain expertise?                    | group discussion |           |           |           |


## Topic 1: Annotation Process (Klie 2024, §3.1)

| Criterion                         | Guiding Question                                                                                                                   | Source          | Dataset 1 | Dataset 2 | Dataset 3 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------- | --------- | --------- |
| Planning Phase Documented         | Does the paper document the goal, budget, target quality, and choice of data/annotators decided before annotation?                | Klie 2024, §3.1 |           |           |           |
| Iterative, Batch-based Annotation | Was the data annotated in cycles (batches), with an evaluation after each batch?                                                   | Klie 2024, §3.1 |           |           |           |
| Pilot Study                       | Was a pilot study with a small team and difficult/corner-case instances conducted before the main annotation?                     | Klie 2024, §3.1 |           |           |           |
| Careful Data Selection            | Were the texts selected deliberately and checked for errors, low quality, non-representative content, or bias before annotation?  | Klie 2024, §3.1 |           |           |           |
| Annotation Scheme Design          | Is the annotation scheme (structure, features, tagsets) documented, suited to the task, and revised when needed?                  | Klie 2024, §3.1 |           |           |           |
| Guideline Design & Refinement     | Were the guidelines carefully designed (or adapted from existing ones), documented, and refined/clarified during the process?     | Klie 2024, §3.1 |           |           |           |
| Quality Evaluation per Batch      | Is annotation quality measured after each batch (e.g., inter-annotator agreement, gold-standard comparison, expert inspection)?   | Klie 2024, §3.1 |           |           |           |
| Validation Step                   | Is there a separate step after annotation and before adjudication that checks whether annotations are correct (direct/indirect)? | Klie 2024, §3.1 |           |           |           |
| Rectifying Measures               | Were corrective measures taken when quality was insufficient (e.g., retraining annotators, clarifying guidelines, re-annotation)? | Klie 2024, §3.1 |           |           |           |
| Adjudication / Gold Standard      | Were multiple annotations merged into one final label per instance only after sufficient quality was reached?                    | Klie 2024, §3.1 |           |           |           |
| Process Stability                 | Was the annotation setup stable before scaling up (larger batches, less rigorous quality control)?                                | Klie 2024, §3.1 |           |           |           |


## Topic 2: Annotator Management (Klie 2024, §3.2)

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
| --- | --- | --- | --- | --- | --- |
| Workforce Selection & Fit | Was the workforce type (crowdworkers, contractors, domain experts) chosen to match task difficulty, language, and required expertise, and was this choice validated (e.g., via a pilot study)? | Klie 2024, §3.2 | | | |
| Qualification Filtering | If qualification filters were used (e.g., acceptance rate, number of completed tasks), were the thresholds grounded (e.g., via a pilot study) rather than set excessively high? | Klie 2024, §3.2 | | | |
| Qualification Testing | Did annotators have to pass a (paid) qualification test, checked against known answers or by experts, before joining the main annotation? | Klie 2024, §3.2 | | | |
| Annotator Training | Were all annotators (including domain experts) trained on the task and guidelines before starting to annotate? | Klie 2024, §3.2 | | | |
| Annotator Debriefing | Were annotators asked for feedback during and after the project (e.g., on guideline clarity, scheme, tool usability)? | Klie 2024, §3.2 | | | |
| Monetary Incentives & Bonuses | If bonuses were offered (e.g., for performance on control questions or task retention), were the rules transparent, communicated beforehand, and not changed afterwards? | Klie 2024, §3.2 | | | |
| Fair Pay & Ethical Treatment | Were annotators paid fairly and treated respectfully (e.g., no unjustified withholding of payment)? | Klie 2024, §3.2 & §3.4 | | | |


## Topic 3: Quality Improvement & Adjudication (Klie 2024, §3.4 & §3.5)

| Criterion                       | Guiding Question                                                                                                          | Source          | Dataset 1 | Dataset 2 | Dataset 3 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------- | --------- | --------- | --------- |
| Manual Correction               | Were low-quality batches corrected (by the original or, for difficult instances, more experienced annotators) instead of being kept as-is? | Klie 2024, §3.4 |           |           |           |
| Updating Guidelines             | Were guidelines or scheme updated when they proved ambiguous or incomplete, and were affected annotations revised?       | Klie 2024, §3.4 |           |           |           |
| Data Filtering                  | Were ambiguous or low-quality instances filtered out, and is the filtering justified and documented?                     | Klie 2024, §3.4 |           |           |           |
| Annotator Feedback              | Did annotators receive feedback on their errors after a batch?                                                            | Klie 2024, §3.4 |           |           |           |
| Annotator Deboarding            | Were annotators who repeatedly delivered low-quality work removed, their annotations redone, and their work still paid?  | Klie 2024, §3.4 |           |           |           |
| Automatic Error Detection       | Were automatic checks used to find annotation errors, and were they validated by humans?                                 | Klie 2024, §3.4 |           |           |           |
| Multiple Labels & Raw Data      | Were multiple labels collected per instance, and are the raw (non-adjudicated) annotations published as well?            | Klie 2024, §3.5 |           |           |           |
| Adjudication Method             | Is the method stated (manual curation, majority voting, probabilistic aggregation) and how ties are handled?             | Klie 2024, §3.5 |           |           |           |


## Topic 4: Quality Estimation & Inter-Annotator Agreement (Klie 2024, §3.3; Day 3)

An IAA value alone says little: our annotation experiment reached S = 0.83 but κ = 0.72 on the same labels, and in the fake-data simulation guessing annotators reached S = 0.81 at 5 % prevalence (Task 2/3). The criteria below check whether a reported IAA value can actually be interpreted.

| Criterion                         | Guiding Question                                                                                                                                                  | Source                          | Dataset 1 | Dataset 2 | Dataset 3 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------- | --------- | --------- |
| IAA Reported                      | Is inter-annotator agreement reported at all, overall and per batch / per label?                                                                                  | Klie 2024, §3.3                 |           |           |           |
| Metric Named & Chance-corrected   | Is the metric explicitly named, and is it chance-corrected (not only percentage agreement, which overestimates agreement)?                                        | Day 3 slides                    |           |           |           |
| Metric Suitability                | Does the metric fit the setup (2 annotators → Cohen's κ, more → Fleiss' κ, missing labels → Krippendorff's α), and is the choice justified?                       | Day 3 slides; James 2026        |           |           |           |
| Label Distribution Reported       | Is the label distribution (prevalence) reported? With skewed labels, S and AC1 are inflated and κ is deflated, so the value cannot be interpreted without it.     | Own experiment (Task 2/3)       |           |           |           |
| Multiple Metrics                  | Are several metrics reported (e.g., percentage agreement + κ + AC1), or is it argued why one is sufficient?                                                       | Own experiment (Task 3)         |           |           |           |
| IAA Setup Documented              | Is it stated how many annotators labeled how many instances (N) for the IAA computation, and whether all instances or only a subset were double-annotated?        | Klie 2024, §3.3                 |           |           |           |
| Before vs. After Adjudication     | Is it clear whether IAA was measured on independent annotations or after discussion/adjudication (which inflates agreement, e.g., our S rose from 0.83 to 0.95)?  | Own experiment (Task 3)         |           |           |           |
| Uncertainty of the Estimate       | Are sample size and confidence intervals (or another uncertainty estimate) given, especially for small batches?                                                    | Chew et al.                     |           |           |           |
| Agreement vs. Correctness         | Is quality also checked against gold-standard/control instances or expert judgment, since annotators can agree and still both be wrong?                           | Klie 2024, §3.3; Day 3 slides   |           |           |           |


## Topic 5: Annotator Operations, Welfare & Audit Fairness (Informed by Lúcio 2026)

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
| --- | --- | --- | --- | --- | --- |
| Annotator Psychological Safeguards | If instances contained toxic, graphic, violent, or sensitive material, were proactive mental health safeguards implemented (e.g., opt-out rights, visual blur filters, mandatory paid counseling), and did well-being sessions count toward working hours? | Lúcio 2026, Part 1 & 2 | | | |
| Modality-Adaptive Pacing & Time Sufficiency | Were speed expectations or throughput quotas grounded in empirical task complexity (e.g., duration of audio/video, text length, difficulty) rather than rigid, homogenized pacing targets? | Lúcio 2026, Part 2 & 4 | | | |
| Overhead & Capacity Accounting | Were essential non-annotation activities (e.g., studying guideline updates, attending calibration sessions, taking physical/restroom breaks) counted as active working time rather than uncompensated downtime? | Lúcio 2026, Part 2 & 4 | | | |
| Audit Sample Validity & Fairness | Were quality assurance (QA) audits performed on statistically representative sample sizes with documented uncertainty intervals, and did auditors evaluate under operational constraints comparable to the frontline annotators? | Lúcio 2026, Part 2 | | | |
| Bidirectional Review & Dispute Resolution | Was there a formalized appeal or discussion workflow where annotators could contest auditor overrides, explain cultural or linguistic context, and clarify ambiguous edge cases? | Lúcio 2026, Part 3 | | | |
| Transparent, Absolute Performance Rubrics | Were annotators evaluated against absolute, criterion-referenced rubrics rather than forced grading curves (stack ranking) or opaque peer comparisons that create blind competition? | Lúcio 2026, Part 4 | | | |
| Frontline Context & Evasion Harvesting | Was there a mechanism for annotators to systematically flag emerging circumvention tactics, cultural slang, or nuanced edge cases to update data schemas and downstream model training? | Lúcio 2026, Part 5 | | | |