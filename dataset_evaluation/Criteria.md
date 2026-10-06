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
| Workforce Selection & Fit | Was the workforce type (crowdworkers, contractors, domain experts, volunteers) appropriately selected to match task difficulty, language, and domain requirements, and was this choice validated (e.g., via a pilot study)? | Klie 2024, §3.2 | | | |
| Qualification Filtering | Were prerequisite qualification filters (e.g., acceptance rate, completed tasks, language proficiency) established without imposing excessively restrictive or ungrounded thresholds? | Klie 2024, §3.2 | | | |
| Qualification Testing | Were annotators evaluated via a dedicated (paid) qualification test on representative or unseen instances to verify proficiency before admission to the main task? | Klie 2024, §3.2 | | | |
| Annotator Training | Was comprehensive task training conducted for all annotator groups—including domain experts and crowdworkers alike—to ensure guideline comprehension and temporal stability? | Klie 2024, §3.2 | | | |
| Annotator Debriefing & Feedback | Were annotators systematically debriefed during and after the project to gather feedback on guideline clarity, scheme edge cases, and tool usability? | Klie 2024, §3.2 | | | |
| Monetary Incentives & Bonuses | Were bonus monetary incentives provided (e.g., for task retention or high performance on control instances) using transparent, pre-communicated rules that avoid gaming? | Klie 2024, §3.2 | | | |
| Fair Pay & Ethical Treatment | Were annotators compensated with fair base pay and treated ethically (e.g., clear terms, respectful communication, and no unjustified wage withholding)? | Klie 2024, §3.2 | | | |


## Topic 3: Quality Improvement & Adjudication (Klie 2024, §3.4 & §3.5)

| Criterion                       | Guiding Question                                                                                                          | Source          | Dataset 1 | Dataset 2 | Dataset 3 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------- | --------- | --------- | --------- |
| Manual Correction               | Were low-quality batches returned to the annotators or routed to more experienced annotators for correction?             | Klie 2024, §3.4 |           |           |           |
| Updating Guidelines             | Were guidelines or scheme updated when they proved ambiguous or incomplete, and were affected annotations revised?       | Klie 2024, §3.4 |           |           |           |
| Data Filtering                  | Were ambiguous or low-quality instances filtered out, and is the filtering justified and documented?                     | Klie 2024, §3.4 |           |           |           |
| Annotator Feedback              | Did annotators receive feedback on their errors after a batch?                                                            | Klie 2024, §3.4 |           |           |           |
| Annotator Deboarding            | Were annotators who repeatedly delivered low-quality work removed, their annotations redone, and their work still paid?  | Klie 2024, §3.4 |           |           |           |
| Automatic Error Detection       | Were automatic checks used to find annotation errors, and were they validated by humans?                                 | Klie 2024, §3.4 |           |           |           |
| Multiple Labels & Raw Data      | Were multiple labels collected per instance, and are the raw (non-adjudicated) annotations published as well?            | Klie 2024, §3.5 |           |           |           |
| Adjudication Method             | Is the method stated (manual curation, majority voting, probabilistic aggregation) and how ties are handled?             | Klie 2024, §3.5 |           |           |           |
