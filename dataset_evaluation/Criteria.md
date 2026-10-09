# Dataset Evaluation

Criteria are grouped by the areas agreed on in the evaluation criteria board (Day 5): Annotation Planning, Data Sourcing, Annotation Process, Annotators, Working Conditions, Quality Assurance, and Adjudication. All criteria of the Klie (2024) annotation guideline (App. 2) are included; "group discussion" in the Source column marks criteria (or parts of them) that come from the board.


## Annotation Planning

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Planning Phase Documented | Does the paper document the goal, budget, target quality, and choice of data/annotators decided before annotation? | Klie 2024, §3.1; group discussion | | | |
| Task Type | Is the task annotation (assigning labels), text production (writing text), or both? This determines which quality measures apply (e.g., agreement and adjudication only for labels). | Klie 2024, App. 2.2 | | | |
| Task Specificity | Are the data instances sufficiently specific, well-scoped, and tailored to the target task? | group discussion | | | |
| Scheme & Guideline Design | Are the annotation scheme (structure, tagsets) and guidelines documented, suited to the task, and carefully designed or adapted from existing ones? | Klie 2024, §3.1; group discussion | | | |
| Annotation Guidelines Available | Are the complete annotation guidelines available in the paper, appendix, or supplementary material (ideally published open access alongside the dataset)? Supplementary material counts only if referenced and findable. | Klie 2024, App. 2.6; group discussion | | | |
| Annotation Scheme Available | Is the annotation scheme (tagset, task description) described in the paper, appendix, or supplementary material? | Klie 2024, App. 2.6 | | | |
| Annotation Interface Available | Is a screenshot of the annotation interface, including the task description shown to annotators, given in the paper, appendix, or supplementary material? | Klie 2024, App. 2.6 | | | |


## Data Sourcing

Ordered by the sub-areas on the board: Source, Collection/Legality/Privacy, Data Content.

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Provenance & Source Credibility | Where do the data originate, is the source credible and trustworthy, and is the collection lineage fully documented? | group discussion | | | |
| Careful Data Selection | Were the data selected deliberately, representative of the target domain, and checked for errors, low quality, or bias (e.g., demographic, geographic, sampling) before annotation? | Klie 2024, §3.1; group discussion | | | |
| Data Filtering (Pre-Annotation) | Is data filtered before annotation via automatic or manual checks? | Klie 2024, App. 2.4.1; group discussion | | | |
| Privacy & Regulatory Compliance | Does the dataset adhere to privacy regulations (e.g., GDPR) and exclude personally identifiable information (PII)? | group discussion | | | |
| Ethical Data Collection | Was the data collected ethically, i.e., with consent of the people involved and respecting licenses, copyright, and platform terms of service? | group discussion | | | |
| Data Correctness | Are the data factually correct and fact-checked, and is the amount of noise (erroneous or corrupted instances) low and documented? | group discussion | | | |
| Diversity, Representation & Objectivity | Is the dataset audited for demographic, linguistic, geographic, or cultural diversity, are subgroups balanced rather than over-representing dominant distributions, and is the content objective rather than one-sided? | group discussion | | | |
| Dataset Ambiguity & Inherent Subjectivity | Does the paper distinguish between genuine annotator error and valid semantic ambiguity / human perspectivism, and is task difficulty or disagreement preserved rather than discarded as noise? | group discussion | | | |
| Contextual Completeness | Are the records complete, and is adequate context preserved to interpret each instance accurately? | group discussion | | | |
| Content Safety & Moderation | Is the dataset screened and free of disturbing, toxic, or offensive content? | group discussion | | | |
| Temporal Currency | Are the data up to date and temporally valid for time-sensitive domains (e.g., statutes, medical facts, news)? | group discussion | | | |


## Annotation Process

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Manual Annotation | Does the dataset involve humans as annotators or as validators (e.g., creating labels, writing text, or only validating automatically generated data)? | Klie 2024, App. 2.1 | | | |
| Iterative Annotation Process | Is an iterative feedback loop used, i.e., was the data annotated in batches, each evaluated before continuing, with scaling up (larger batches, lighter quality control) only once the setup was stable? | Klie 2024, App. 2.4.1 & §3.1; Hovy and Lavid 2010; Pustejovsky and Stubbs 2013; Monarch 2021; group discussion | | | |
| Pilot Study | Were one or more pilot studies with a small team and difficult/corner-case instances conducted before the main annotation? | Klie 2024, App. 2.4.1 & §3.1; group discussion | | | |
| Validation | Is there an explicit validation step after annotation and before adjudication that checks whether annotations are correct? | Klie 2024, App. 2.4.1 & §3.1; group discussion | | | |


## Annotators

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Annotator Type | Are the annotators experts, contractors, crowdworkers, or volunteers? | Klie 2024, App. 2.3 | | | |
| Workforce Selection & Expertise | Was the workforce type chosen to match task difficulty, language, and required expertise, and was this choice validated (e.g., via a pilot study)? | Klie 2024, §3.2; group discussion | | | |
| Role Separation & Expertise Hierarchy | Was there a clear separation of duties between frontline annotators, domain expert reviewers, quality auditors, and tie-breaking adjudicators, with expert credentials documented? | group discussion | | | |
| Qualification Filter | Were annotators filtered by criteria such as native language, location, acceptance rate, or number of completed tasks, and were these filters grounded rather than set excessively high? | Klie 2024, App. 2.4.2 & §3.2; Kummerfeld 2021; group discussion | | | |
| Qualification Test | Did annotators have to pass a (paid) qualification test, checked against known answers or by experts, before taking part in the annotation itself? | Klie 2024, App. 2.4.2 & §3.2; Kummerfeld 2021; group discussion | | | |
| Annotator Training | Were all annotators (including domain experts) trained on the task and guidelines before starting to annotate? | Klie 2024, App. 2.4.2 & §3.2; Bayerl and Paul 2011; group discussion | | | |
| Monetary Incentive | Do annotators receive additional payment for exceptional quality, and were the bonus rules transparent, communicated beforehand, not changed afterwards, and not gameable at the expense of quality? | Klie 2024, App. 2.4.2 & §3.2; group discussion | | | |
| Annotator Debriefing | Did annotators give feedback to improve the annotation process, during and after the project (e.g., on guideline clarity, scheme, tool usability)? | Klie 2024, App. 2.4.4 & §3.2; Neuendorf 2016; group discussion | | | |
| Annotator Voice | Could annotators contest audit decisions, explain cultural or linguistic context, and report new edge cases or circumvention tactics so that guidelines and schema are updated? | Lúcio 2026, Part 3 & 5; group discussion | | | |
| Annotator Deboarding | Were annotators who repeatedly delivered low-quality work removed from the labor pool and their annotations redone? | Klie 2024, App. 2.4.4 & §3.4; Hsueh et al. 2009; group discussion | | | |


## Working Conditions

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Fair Pay & Ethical Treatment | Were annotators paid fairly and treated respectfully (e.g., no unjustified withholding of payment, also when deboarded)? | Klie 2024, §3.2 & §3.4; group discussion | | | |
| Psychological Safeguards | If annotators were exposed to toxic, graphic, or violent content, were mental-health safeguards in place (e.g., opt-out, blurring, paid counseling)? | Lúcio 2026, Part 1 & 2; group discussion | | | |
| Realistic Workload & Working Time | Were speed/throughput targets based on actual task effort (e.g., video length, difficulty) rather than uniform quotas, were annotators not put under excessive time pressure, and did mandatory non-annotation activities (guideline meetings, well-being sessions, breaks) count as paid working time? | Lúcio 2026, Part 2 & 4; group discussion | | | |
| Audit Sample Validity & Fairness | Were quality audits of individual annotators based on sufficiently large samples, and did auditors work under conditions comparable to the annotators (e.g., time pressure)? | Lúcio 2026, Part 2; group discussion | | | |
| Transparent, Absolute Performance Rubrics | Were annotators' performance and KPIs evaluated fairly against absolute, transparent criteria rather than forced grading curves (stack ranking) or opaque peer comparisons? | Lúcio 2026, Part 4; group discussion | | | |


## Quality Assurance

An IAA value alone says little: our annotation experiment reached S = 0.83 but κ = 0.72 on the same labels, and in the fake-data simulation guessing annotators reached S = 0.81 at 5 % prevalence (Task 2/3). The agreement criteria below check whether a reported IAA value can actually be interpreted.

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Correction | Were instances improved or corrected, e.g., low-quality batches corrected by the original or, for difficult instances, more experienced annotators instead of being kept as-is? | Klie 2024, App. 2.4.4 & §3.4; group discussion | | | |
| Automatic Checks | Were automatic checks (e.g., spell checking, hand-crafted rules) used to find annotation errors, and were they validated by humans? | Klie 2024, App. 2.4.4 & §3.4; group discussion | | | |
| Indirect Annotation | Does the annotation process have several steps, where later ones indirectly validate earlier ones? | Klie 2024, App. 2.4.1 | | | |
| Validation Performed | Is a validation of the annotations actually performed and reported? | Klie 2024, App. 2.9 | | | |
| Validator Type | Who validated: experts, contractors, crowdworkers, volunteers, or the annotators themselves? | Klie 2024, App. 2.9-2.10 | | | |
| Validation Inspection Size | How many instances were validated, and how large is the full dataset (0 for both if the whole dataset)? Is this sample size statistically justified rather than an arbitrary spot-check? | Klie 2024, App. 2.10.1; group discussion | | | |
| Give Annotators Feedback | Did annotators receive (timely, constructive) feedback on their errors to improve their annotation quality, e.g., after each batch? | Klie 2024, App. 2.4.4 & §3.4; group discussion | | | |
| Control Questions | Were control questions with known answers (gold instances, attention checks, honeypots) injected to estimate annotator and task performance and to detect bots, spammers, or fatigue? | Klie 2024, App. 2.4.3; Callison-Burch and Dredze 2010; group discussion | | | |
| Error Rate | Is the error rate computed for the final, adjudicated corpus? | Klie 2024, App. 2.4.3; Monarch 2021 | | | |
| Error Rate Value | What error rate (incorrect / total instances) is reported for the adjudicated dataset? (Use -1 if used but no value is given.) | Klie 2024, App. 2.11.1 | | | |
| Error Rate Inspection Size | On how many instances was the error rate computed, and how large is the full dataset (0 for both if the whole dataset)? Is the sample statistically justified (e.g., with a confidence interval)? | Klie 2024, App. 2.11.2; group discussion | | | |
| Agreement vs. Correctness | Is quality also checked against control/gold instances or by manual inspection, since annotators can agree and still both be wrong? | Klie 2024, §3.3; Day 3 slides; group discussion | | | |
| Case & Value Completeness | Does the dataset thoroughly cover domain edge cases, rare classes, and full feature values (with missing, corrupted, or incomplete attributes documented and quantified)? | group discussion | | | |
| Agreement | Is at least one inter-annotator agreement measure used for the annotation or validation (not only the pilot study), and is it reported overall and per batch / per label? | Klie 2024, App. 2.4.3 & §3.3; Krippendorff 2004; Artstein and Poesio 2008; group discussion | | | |
| Agreement Measure | Which measure is used: percent agreement, Cohen's κ, Fleiss' κ, Krippendorff's α (unitized), Pearson's r, Spearman's ρ, Kendall's τ, ICC, precision, recall, or F1? (Mark ? if unclear.) | Klie 2024, App. 2.8.1 | | | |
| Metric Choice | Is the metric chance-corrected (not only percentage agreement), suited to the setup (2 annotators → Cohen's κ, more → Fleiss' κ, missing labels → Krippendorff's α), and are several metrics reported or the choice justified? | Klie 2024, §3.3; Day 3 slides; James 2026; own experiment (Task 3) | | | |
| Agreement Value | What agreement value is reported for the final dataset (not the pilot)? (Use -1 if agreement is used but no value is given.) | Klie 2024, App. 2.8.2 | | | |
| Label Distribution Reported | Is the label distribution (prevalence) reported? With skewed labels, S and AC1 are inflated and κ is deflated, so the value cannot be interpreted without it. | Own experiment (Task 2/3) | | | |
| Agreement Inspection Size | On how many instances was agreement computed, and how large is the full dataset? (0 for both if the whole dataset.) | Klie 2024, App. 2.8.3 | | | |
| IAA Setup & Uncertainty | Is it stated how many annotators labeled how many instances, whether all or only a subset was multiply annotated, and is an uncertainty estimate (e.g., confidence interval) given? | Klie 2024, §3.3; Chew et al. | | | |
| Agreement Interpretation: Literature | Is the value interpreted using ranges from the literature (e.g., Landis and Koch 1977; Krippendorff 1980)? | Klie 2024, App. 2.8.4 | | | |
| Agreement Interpretation: Custom | Does the paper claim a quality level such as sufficient, high, or good without citing any work, and is this justified for the domain? | Klie 2024, App. 2.8.4 | | | |
| Agreement Interpretation: Compares to Previous | Does the paper compare its agreement to that of a similar, earlier dataset? | Klie 2024, App. 2.8.4 | | | |
| Agreement Filter | Are instances filtered out if agreement is too low (e.g., a rolling threshold during annotation that flags low-consensus items or drifting annotators)? | Klie 2024, App. 2.4.4; group discussion | | | |
| Manual Filter | Are instances filtered out manually (e.g., after inspecting low-agreement items)? | Klie 2024, App. 2.4.4; group discussion | | | |
| Time Filter | Are instances filtered out because annotators annotated improbably quickly (e.g., minimum duration thresholds to discard "speeders")? | Klie 2024, App. 2.4.4; Ferracane et al. 2021; group discussion | | | |
| Data Filtering (Post-Annotation) | Were ambiguous or low-quality annotated instances filtered out, and is the filtering justified and documented? | Klie 2024, §3.4; group discussion | | | |
| Guideline Refinement | Were the guidelines or the scheme refined when they proved ambiguous or incomplete, were affected annotations revised, and is the quality of the final guidelines adequate? | Klie 2024, App. 2.4.4 & §3.4; group discussion | | | |
| Overall Judgement | Considering all quality management performed and reported, is it excellent (iterative process, training, agreement and error rate, extensive validation, continuous human inspection), sufficient (some of these, at least some validation and manual inspection), or subpar (none of these; quality relies at most on aggregation)? | Klie 2024, App. 2.7 | | | |


## Adjudication

| Criterion | Guiding Question | Source | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|
| Adjudication | Was adjudication (merging multiple annotations per instance into one) done only after sufficient quality was reached, and is the method stated? | Klie 2024, App. 2.5 & §3.5; group discussion | | | |
| Majority Voting | Is the label assigned by at least half of the annotators chosen (or, as total agreement, only unanimous labels kept)? | Klie 2024, App. 2.5; Paun et al. 2018; group discussion | | | |
| Manual Tie Breaking | Does a human inspect and curate instances that have no majority? | Klie 2024, App. 2.5; group discussion | | | |
| Dawid-Skene | Is a probabilistic aggregation model of annotator expertise (Dawid-Skene) used? | Klie 2024, App. 2.5; Dawid and Skene 1979; group discussion | | | |
| MACE | Is a probabilistic model of annotator expertise and spamming likelihood (MACE) used? | Klie 2024, App. 2.5; Hovy et al. 2013; group discussion | | | |
| Manual Curation | Does a human manually inspect and curate instances? | Klie 2024, App. 2.5; Bareket and Tsarfaty 2021; group discussion | | | |
| N/A | Is adjudication not applicable because there is only one annotation per instance or the task is text production? | Klie 2024, App. 2.5; group discussion | | | |
| Unclear Adjudication | Is adjudication not mentioned although it must have happened (e.g., several annotations per instance)? | Klie 2024, App. 2.5; group discussion | | | |
| Multiple Labels & Raw Data | Were multiple labels collected per instance, and are the raw (non-adjudicated) annotations published as well? | Klie 2024, §3.5; group discussion | | | |
| Before vs. After Adjudication | Is it clear whether IAA was measured on independent annotations or after discussion/adjudication (which inflates agreement, e.g., our S rose from 0.83 to 0.95)? | Own experiment (Task 3); group discussion | | | |
