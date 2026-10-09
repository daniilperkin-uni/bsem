# Dataset Evaluation


## Group Discussion

Criteria from the group discussion that are covered in more detail by a literature-based topic below were moved there (marked with "group discussion" in the Source column).

| Criterion                       | Guiding Question                                                                                                   | Source           | Dataset 1 | Dataset 2 | Dataset 3 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- | --------- | --------- | --------- |
| Data Correctness                | Are the data factually correct and fact-checked?                                                                   | group discussion |           |           |           |
| Content Safety & Moderation     | Is the dataset screened and free of disturbing, toxic, or offensive content?                                       | group discussion |           |           |           |
| Task Specificity                | Are the data instances sufficiently specific, well-scoped, and tailored to the target task?                        | group discussion |           |           |           |
| Provenance & Source Credibility | Where do the data originate, is the source credible, and is the collection lineage fully documented?               | group discussion |           |           |           |
| Privacy & Regulatory Compliance | Does the dataset adhere to privacy regulations (e.g., GDPR) and exclude personally identifiable information (PII)? | group discussion |           |           |           |
| Temporal Currency               | Are the data up to date and temporally valid for time-sensitive domains (e.g., statutes, medical facts, news)?     | group discussion |           |           |           |
| Contextual Completeness         | Are the records complete, and is adequate context preserved to interpret each instance accurately?                 | group discussion |           |           |           |


## Topic 1: Annotation Process (Klie 2024, §3.1)

| Criterion                 | Guiding Question                                                                                                                                                                     | Source                            | Dataset 1 | Dataset 2 | Dataset 3 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | --------- | --------- | --------- |
| Planning Phase Documented | Does the paper document the goal, budget, target quality, and choice of data/annotators decided before annotation?                                                                   | Klie 2024, §3.1                   |           |           |           |
| Iterative Batch Process   | Was the data annotated in batches, each evaluated before continuing, with scaling up (larger batches, lighter quality control) only once the setup was stable?                       | Klie 2024, §3.1                   |           |           |           |
| Pilot Study               | Was a pilot study with a small team and difficult/corner-case instances conducted before the main annotation?                                                                        | Klie 2024, §3.1                   |           |           |           |
| Careful Data Selection    | Were the texts selected deliberately, representative of the target domain, and checked for errors, low quality, or bias (e.g., demographic, geographic, sampling) before annotation? | Klie 2024, §3.1; group discussion |           |           |           |
| Scheme & Guideline Design | Are the annotation scheme (structure, tagsets) and guidelines documented, suited to the task, and carefully designed or adapted from existing ones?                                  | Klie 2024, §3.1                   |           |           |           |
| Validation Step           | Is there a separate step after annotation and before adjudication that checks whether annotations are correct (direct/indirect)?                                                     | Klie 2024, §3.1                   |           |           |           |


## Topic 2: Annotator Management (Klie 2024, §3.2)

| Criterion                         | Guiding Question                                                                                                                                                                               | Source                                   | Dataset 1 | Dataset 2 | Dataset 3 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | --------- | --------- | --------- |
| Workforce Selection & Expertise   | Was the workforce type (crowdworkers, contractors, domain experts) chosen to match task difficulty, language, and required expertise, and was this choice validated (e.g., via a pilot study)? | Klie 2024, §3.2; group discussion        |           |           |           |
| Qualification Filtering & Testing | Did annotators pass a (paid) qualification test checked against known answers or by experts, and were platform filters (e.g., acceptance rate) grounded rather than set excessively high?      | Klie 2024, §3.2                          |           |           |           |
| Annotator Training                | Were all annotators (including domain experts) trained on the task and guidelines before starting to annotate?                                                                                 | Klie 2024, §3.2                          |           |           |           |
| Annotator Debriefing              | Were annotators asked for feedback during and after the project (e.g., on guideline clarity, scheme, tool usability)?                                                                          | Klie 2024, §3.2                          |           |           |           |
| Monetary Incentives & Bonuses     | If bonuses were offered, were the rules transparent, communicated beforehand, not changed afterwards, and not gameable at the expense of quality?                                              | Klie 2024, §3.2                          |           |           |           |
| Fair Pay & Ethical Treatment      | Were annotators paid fairly and treated respectfully (e.g., no unjustified withholding of payment, also when deboarded)?                                                                       | Klie 2024, §3.2 & §3.4; group discussion |           |           |           |


## Topic 3: Quality Improvement & Adjudication (Klie 2024, §3.4 & §3.5)

| Criterion                  | Guiding Question                                                                                                                                                               | Source                 | Dataset 1 | Dataset 2 | Dataset 3 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | --------- | --------- | --------- |
| Manual Correction          | Were low-quality batches corrected (by the original or, for difficult instances, more experienced annotators) instead of being kept as-is?                                     | Klie 2024, §3.4        |           |           |           |
| Updating Guidelines        | Were guidelines or scheme updated when they proved ambiguous or incomplete, and were affected annotations revised?                                                             | Klie 2024, §3.4        |           |           |           |
| Data Filtering             | Were ambiguous or low-quality instances filtered out, and is the filtering justified and documented?                                                                           | Klie 2024, §3.4        |           |           |           |
| Annotator Feedback         | Did annotators receive feedback on their errors after a batch?                                                                                                                 | Klie 2024, §3.4        |           |           |           |
| Annotator Deboarding       | Were annotators who repeatedly delivered low-quality work removed and their annotations redone?                                                                                | Klie 2024, §3.4        |           |           |           |
| Automatic Error Detection  | Were automatic checks used to find annotation errors, and were they validated by humans?                                                                                       | Klie 2024, §3.4        |           |           |           |
| Multiple Labels & Raw Data | Were multiple labels collected per instance, and are the raw (non-adjudicated) annotations published as well?                                                                  | Klie 2024, §3.5        |           |           |           |
| Adjudication               | Was adjudication done only after sufficient quality was reached, is the method stated (manual curation, majority voting, probabilistic aggregation), and how are ties handled? | Klie 2024, §3.1 & §3.5 |           |           |           |


## Topic 4: Quality Estimation & Inter-Annotator Agreement (Klie 2024, §3.3; Day 3)

An IAA value alone says little: our annotation experiment reached S = 0.83 but κ = 0.72 on the same labels, and in the fake-data simulation guessing annotators reached S = 0.81 at 5 % prevalence (Task 2/3). The criteria below check whether a reported IAA value can actually be interpreted.

| Criterion                     | Guiding Question                                                                                                                                                                                                                      | Source                                                             | Dataset 1 | Dataset 2 | Dataset 3 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------- | --------- | --------- |
| IAA Reported                  | Is inter-annotator agreement reported at all, overall and per batch / per label?                                                                                                                                                      | Klie 2024, §3.3; group discussion                                  |           |           |           |
| Metric Choice                 | Is the metric named, chance-corrected (not only percentage agreement), suited to the setup (2 annotators → Cohen's κ, more → Fleiss' κ, missing labels → Krippendorff's α), and are several metrics reported or the choice justified? | Klie 2024, §3.3; Day 3 slides; James 2026; own experiment (Task 3) |           |           |           |
| Label Distribution Reported   | Is the label distribution (prevalence) reported? With skewed labels, S and AC1 are inflated and κ is deflated, so the value cannot be interpreted without it.                                                                         | Own experiment (Task 2/3)                                          |           |           |           |
| IAA Setup & Uncertainty       | Is it stated how many annotators labeled how many instances (N), whether all or only a subset was double-annotated, and is an uncertainty estimate (e.g., confidence interval) given?                                                 | Klie 2024, §3.3; Chew et al.                                       |           |           |           |
| Before vs. After Adjudication | Is it clear whether IAA was measured on independent annotations or after discussion/adjudication (which inflates agreement, e.g., our S rose from 0.83 to 0.95)?                                                                      | Own experiment (Task 3)                                            |           |           |           |
| Agreement vs. Correctness     | Is quality also checked against control/gold instances or by manual inspection (ideally with an error rate for the final dataset), since annotators can agree and still both be wrong?                                                | Klie 2024, §3.3; Day 3 slides; group discussion                    |           |           |           |


## Topic 5: Annotator Operations, Welfare & Audit Fairness (Informed by Lúcio 2026)

| Criterion                                 | Guiding Question                                                                                                                                                                                                                                 | Source                 | Dataset 1 | Dataset 2 | Dataset 3 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | --------- | --------- | --------- |
| Psychological Safeguards                  | If annotators were exposed to toxic, graphic, or violent content, were mental-health safeguards in place (e.g., opt-out, blurring, paid counseling)?                                                                                             | Lúcio 2026, Part 1 & 2 |           |           |           |
| Realistic Workload & Working Time         | Were speed/throughput targets based on actual task effort (e.g., video length, difficulty) rather than uniform quotas, and did mandatory non-annotation activities (guideline meetings, well-being sessions, breaks) count as paid working time? | Lúcio 2026, Part 2 & 4 |           |           |           |
| Audit Sample Validity & Fairness          | Were quality audits of individual annotators based on sufficiently large samples, and did auditors work under conditions comparable to the annotators (e.g., time pressure)?                                                                     | Lúcio 2026, Part 2     |           |           |           |
| Annotator Voice                           | Could annotators contest audit decisions, explain cultural or linguistic context, and report new edge cases or circumvention tactics so that guidelines and schema are updated?                                                                  | Lúcio 2026, Part 3 & 5 |           |           |           |
| Transparent, Absolute Performance Rubrics | Were annotators evaluated against absolute, transparent criteria rather than forced grading curves (stack ranking) or opaque peer comparisons?                                                                                                   | Lúcio 2026, Part 4     |           |           |           |


## Topic 6: In-Flight Quality Control, Representation & Open Science (Evaluation Criteria Board)

This topic covers operational in-process controls, corpus completeness/diversity, open science reproducibility, and formal quality benchmarking identified from the evaluation criteria board.

| Criterion                                 | Guiding Question                                                                                                                                                                             | Source                    | Dataset 1 | Dataset 2 | Dataset 3 |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------- | --------- | --------- |
| Control Questions & Attention Checks      | Were attention checks, gold-standard trap instances, or honeypot questions embedded during annotation to detect automated bots, spammers, or annotator fatigue in real time?             | evaluation criteria board |           |           |           |
| In-Flight Time & Speed Filtering          | Were task completion times tracked and filtered (e.g., minimum duration thresholds to discard "speeders" who answer without reading, or flags for annotators under extreme time pressure)? | evaluation criteria board |           |           |           |
| Dynamic Agreement & Quality Filtering     | Was an active agreement filter or rolling performance threshold applied during the annotation process to detect and flag drifting annotators or low-consensus items before adjudication?     | evaluation criteria board |           |           |           |
| Guideline Availability & Open Artifacts   | Are the complete annotation guidelines, codebooks, schema definitions, and labeling interface templates published open-access alongside the dataset for auditability and reproducibility?  | evaluation criteria board |           |           |           |
| Dataset Diversity & Representation        | Is the dataset explicitly audited for demographic, linguistic, geographic, or cultural diversity, and are subgroups balanced rather than over-representing dominant distributions?       | evaluation criteria board |           |           |           |
| Case & Value Completeness                 | Does the dataset thoroughly cover domain edge cases, rare classes, and full feature values (with missing, corrupted, or incomplete attributes documented and quantified)?                  | evaluation criteria board |           |           |           |
| Dataset Ambiguity & Inherent Subjectivity | Does the paper distinguish between genuine annotator error and valid semantic ambiguity / human perspectivism, and is task difficulty or disagreement preserved rather than discarded as noise?         | evaluation criteria board |           |           |           |
| Role Separation & Expertise Hierarchy     | Was there a clear hierarchical separation of duties between frontline annotators, domain expert reviewers, quality auditors, and tie-breaking adjudicators, with expert credentials documented?         | evaluation criteria board |           |           |           |
| Agreement Benchmarking & Interpretation   | Is the reported agreement value benchmarked against established literature thresholds (e.g., Landis & Koch), previous comparable state-of-the-art annotation efforts, or justified domain-specific baselines?            | evaluation criteria board |           |           |           |
| Audit Sample Sizing & Error Rate Power    | Were validation checks and final dataset error rate estimations performed on a statistically justified inspection sample size with documented confidence intervals, rather than an arbitrary small spot-check?            | evaluation criteria board |           |           |           |

