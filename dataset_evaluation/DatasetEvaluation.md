# Dataset Evaluation

**First**, write a paragraph (ca. 5 sentences) on the use case. (For example Visual Question Answering is the task of answering an question based on an image... It is important because .. We selected it because ... )

Scene understanding is the computer vision task of localizing, segmenting, and recognizing multiple co-occurring objects within their natural everyday contexts. 
It is essential for intelligent systems because interpreting real-world environments requires understanding not only where an object is located, 
but what semantic category it belongs to and how it spatially and functionally relates to its surroundings. 
The primary difficulty stems from non-canonical viewpoints, severe occlusions, 
and cluttered visual scenes that simplified, object-centric benchmarks fail to capture. 
We selected this use case because high-impact applications—such as robotics, autonomous navigation, 
and assistive technologies—fundamentally depend on models trained on complex, contextual scenes rather than isolated, centered subjects. 
Evaluating datasets under this use case allows us to rigorously examine whether granular semantic category specificity 
or massive geometric instance coverage is more critical for robust visual representation.




**Second**, write a paragraph on the 3 most important criteria and why they are most important. (ca. 1 sentence per criterion)
(For example, in VQA, it is important that the questions and images are realistic, because ... )

For Scene Understanding, the three most critical criteria are Task Specificity (Annotation Planning), Careful Data Selection (Data Sourcing), and Data Correctness (Data Sourcing):
First, Task Specificity is essential because true scene understanding requires explicit, well-scoped semantic categories to enable models to recognize distinct functional object identities, whereas purely class-agnostic masks cannot support semantic reasoning or inter-object relational modeling. 
Second, Careful Data Selection is critical because the training imagery must capture complex, non-iconic environments with realistic multi-object co-occurrences and background clutter to prevent models from overfitting to simplified, canonical perspectives. 
Third, Data Correctness is indispensable because resolving dense scenes with severe occlusions and overlapping objects demands verified, pixel-accurate instance boundaries to prevent annotation noise from corrupting downstream models.


| Criterion (Priority 1) | MS COCO | SA-1B | Evaluative Contrast |
|---|---|---|---|
| **Task Specificity** | **High**: Defines 91 mutually agreed entry-level semantic categories (e.g., person, chair, dog) specifically chosen for scene understanding. | **Low / N/A**: Completely class-agnostic. Contains 1.1 billion masks, but zero semantic or category labels. | **COCO clearly wins**: A model trained solely on SA-1B cannot identify what any object is without external semantic grounding. |
| **Careful Data Selection** | **High**: Specifically collected non-iconic photos from Flickr using pairwise queries (`"dog + car"`) to guarantee multi-object contextual scenes. | **High**: Curated 11 million high-resolution photos directly from a commercial photo agency, achieving verified global geographic diversity across 50+ countries. | **Nuanced comparison**: COCO excels in deliberate contextual co-occurrence design; SA-1B excels in global geographic coverage and photographic quality. |
| **Data Correctness** | **High**: Human-annotated polygons filtered through qualification tests, worker deboarding, and 3-to-5 worker verification with honeypots. | **High**: Algorithmic stability ($\delta$) and IoU filtering; human audit of 500 images showed 94% of masks had >90% IoU with expert corrections. | **Methodological contrast**: Human crowd verification with control instances (COCO) vs. scalable automated confidence filtering validated via expert post-hoc audits (SA-1B). |

### Data Sourcing

Ordered by the sub-areas on the board: Source, Collection/Legality/Privacy, Data Content.

| Criterion | Guiding Question | Source | Use Case Priority | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|---|
| Provenance & Source Credibility | Where do the data originate, is the source credible and trustworthy, and is the collection lineage fully documented? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Careful Data Selection | Were the data selected deliberately, representative of the target domain, and checked for errors, low quality, or bias (e.g., demographic, geographic, sampling) before annotation? | Klie 2024, §3.1; group discussion | 1<br>2<br>3<br>N/A | | | |
| Data Filtering (Pre-Annotation) | Is data filtered before annotation via automatic or manual checks? | Klie 2024, App. 2.4.1; group discussion | 1<br>2<br>3<br>N/A | | | |
| Privacy & Regulatory Compliance | Does the dataset adhere to privacy regulations (e.g., GDPR) and exclude personally identifiable information (PII)? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Ethical Data Collection | Was the data collected ethically, i.e., with consent of the people involved and respecting licenses, copyright, and platform terms of service? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Data Correctness | Are the data factually correct and fact-checked, and is the amount of noise (erroneous or corrupted instances) low and documented? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Diversity, Representation & Objectivity | Is the dataset audited for demographic, linguistic, geographic, or cultural diversity, are subgroups balanced rather than over-representing dominant distributions, and is the content objective rather than one-sided? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Dataset Ambiguity & Inherent Subjectivity | Does the paper distinguish between genuine annotator error and valid semantic ambiguity / human perspectivism, and is task difficulty or disagreement preserved rather than discarded as noise? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Contextual Completeness | Are the records complete, and is adequate context preserved to interpret each instance accurately? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Content Safety & Moderation | Is the dataset screened and free of disturbing, toxic, or offensive content? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Temporal Currency | Are the data up to date and temporally valid for time-sensitive domains (e.g., statutes, medical facts, news)? | group discussion | 1<br>2<br>3<br>N/A | | | |


### Annotation Process

| Criterion | Guiding Question | Source | Use Case Priority | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|---|
| Manual Annotation | Does the dataset involve humans as annotators or as validators (e.g., creating labels, writing text, or only validating automatically generated data)? | Klie 2024, App. 2.1 | 1<br>2<br>3<br>N/A | | | |
| Iterative Annotation Process | Is an iterative feedback loop used, i.e., was the data annotated in batches, each evaluated before continuing, with scaling up (larger batches, lighter quality control) only once the setup was stable? | Klie 2024, App. 2.4.1 & §3.1; Hovy and Lavid 2010; Pustejovsky and Stubbs 2013; Monarch 2021; group discussion | 1<br>2<br>3<br>N/A | | | |
| Pilot Study | Were one or more pilot studies with a small team and difficult/corner-case instances conducted before the main annotation? | Klie 2024, App. 2.4.1 & §3.1; group discussion | 1<br>2<br>3<br>N/A | | | |
| Validation | Is there an explicit validation step after annotation and before adjudication that checks whether annotations are correct? | Klie 2024, App. 2.4.1 & §3.1; group discussion | 1<br>2<br>3<br>N/A | | | |


### Annotators

| Criterion | Guiding Question | Source | Use Case Priority | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|---|
| Annotator Type | Are the annotators experts, contractors, crowdworkers, or volunteers? | Klie 2024, App. 2.3 | 1<br>2<br>3<br>N/A | | | |
| Workforce Selection & Expertise | Was the workforce type chosen to match task difficulty, language, and required expertise, and was this choice validated (e.g., via a pilot study)? | Klie 2024, §3.2; group discussion | 1<br>2<br>3<br>N/A | | | |
| Role Separation & Expertise Hierarchy | Was there a clear separation of duties between frontline annotators, domain expert reviewers, quality auditors, and tie-breaking adjudicators, with expert credentials documented? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Qualification Filter | Were annotators filtered by criteria such as native language, location, acceptance rate, or number of completed tasks, and were these filters grounded rather than set excessively high? | Klie 2024, App. 2.4.2 & §3.2; Kummerfeld 2021; group discussion | 1<br>2<br>3<br>N/A | | | |
| Qualification Test | Did annotators have to pass a (paid) qualification test, checked against known answers or by experts, before taking part in the annotation itself? | Klie 2024, App. 2.4.2 & §3.2; Kummerfeld 2021; group discussion | 1<br>2<br>3<br>N/A | | | |
| Annotator Training | Were all annotators (including domain experts) trained on the task and guidelines before starting to annotate? | Klie 2024, App. 2.4.2 & §3.2; Bayerl and Paul 2011; group discussion | 1<br>2<br>3<br>N/A | | | |
| Monetary Incentive | Do annotators receive additional payment for exceptional quality, and were the bonus rules transparent, communicated beforehand, not changed afterwards, and not gameable at the expense of quality? | Klie 2024, App. 2.4.2 & §3.2; group discussion | 1<br>2<br>3<br>N/A | | | |
| Annotator Debriefing | Did annotators give feedback to improve the annotation process, during and after the project (e.g., on guideline clarity, scheme, tool usability)? | Klie 2024, App. 2.4.4 & §3.2; Neuendorf 2016; group discussion | 1<br>2<br>3<br>N/A | | | |
| Annotator Voice | Could annotators contest audit decisions, explain cultural or linguistic context, and report new edge cases or circumvention tactics so that guidelines and schema are updated? | Lúcio 2026, Part 3 & 5; group discussion | 1<br>2<br>3<br>N/A | | | |
| Annotator Deboarding | Were annotators who repeatedly delivered low-quality work removed from the labor pool and their annotations redone? | Klie 2024, App. 2.4.4 & §3.4; Hsueh et al. 2009; group discussion | 1<br>2<br>3<br>N/A | | | |


### Working Conditions

| Criterion | Guiding Question | Source | Use Case Priority | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|---|
| Fair Pay & Ethical Treatment | Were annotators paid fairly and treated respectfully (e.g., no unjustified withholding of payment, also when deboarded)? | Klie 2024, §3.2 & §3.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Psychological Safeguards | If annotators were exposed to toxic, graphic, or violent content, were mental-health safeguards in place (e.g., opt-out, blurring, paid counseling)? | Lúcio 2026, Part 1 & 2; group discussion | 1<br>2<br>3<br>N/A | | | |
| Realistic Workload & Working Time | Were speed/throughput targets based on actual task effort (e.g., video length, difficulty) rather than uniform quotas, were annotators not put under excessive time pressure, and did mandatory non-annotation activities (guideline meetings, well-being sessions, breaks) count as paid working time? | Lúcio 2026, Part 2 & 4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Audit Sample Validity & Fairness | Were quality audits of individual annotators based on sufficiently large samples, and did auditors work under conditions comparable to the annotators (e.g., time pressure)? | Lúcio 2026, Part 2; group discussion | 1<br>2<br>3<br>N/A | | | |
| Transparent, Absolute Performance Rubrics | Were annotators' performance and KPIs evaluated fairly against absolute, transparent criteria rather than forced grading curves (stack ranking) or opaque peer comparisons? | Lúcio 2026, Part 4; group discussion | 1<br>2<br>3<br>N/A | | | |


### Quality Assurance

An IAA value alone says little: our annotation experiment reached S = 0.83 but κ = 0.72 on the same labels, and in the fake-data simulation guessing annotators reached S = 0.81 at 5 % prevalence (Task 2/3). The agreement criteria below check whether a reported IAA value can actually be interpreted.

| Criterion | Guiding Question | Source | Use Case Priority | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|---|
| Correction | Were instances improved or corrected, e.g., low-quality batches corrected by the original or, for difficult instances, more experienced annotators instead of being kept as-is? | Klie 2024, App. 2.4.4 & §3.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Automatic Checks | Were automatic checks (e.g., spell checking, hand-crafted rules) used to find annotation errors, and were they validated by humans? | Klie 2024, App. 2.4.4 & §3.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Indirect Annotation | Does the annotation process have several steps, where later ones indirectly validate earlier ones? | Klie 2024, App. 2.4.1 | 1<br>2<br>3<br>N/A | | | |
| Validation Performed | Is a validation of the annotations actually performed and reported? | Klie 2024, App. 2.9 | 1<br>2<br>3<br>N/A | | | |
| Validator Type | Who validated: experts, contractors, crowdworkers, volunteers, or the annotators themselves? | Klie 2024, App. 2.9-2.10 | 1<br>2<br>3<br>N/A | | | |
| Validation Inspection Size | How many instances were validated, and how large is the full dataset (0 for both if the whole dataset)? Is this sample size statistically justified rather than an arbitrary spot-check? | Klie 2024, App. 2.10.1; group discussion | 1<br>2<br>3<br>N/A | | | |
| Give Annotators Feedback | Did annotators receive (timely, constructive) feedback on their errors to improve their annotation quality, e.g., after each batch? | Klie 2024, App. 2.4.4 & §3.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Control Questions | Were control questions with known answers (gold instances, attention checks, honeypots) injected to estimate annotator and task performance and to detect bots, spammers, or fatigue? | Klie 2024, App. 2.4.3; Callison-Burch and Dredze 2010; group discussion | 1<br>2<br>3<br>N/A | | | |
| Error Rate | Is the error rate computed for the final, adjudicated corpus? | Klie 2024, App. 2.4.3; Monarch 2021 | 1<br>2<br>3<br>N/A | | | |
| Error Rate Value | What error rate (incorrect / total instances) is reported for the adjudicated dataset? (Use -1 if used but no value is given.) | Klie 2024, App. 2.11.1 | 1<br>2<br>3<br>N/A | | | |
| Error Rate Inspection Size | On how many instances was the error rate computed, and how large is the full dataset (0 for both if the whole dataset)? Is the sample statistically justified (e.g., with a confidence interval)? | Klie 2024, App. 2.11.2; group discussion | 1<br>2<br>3<br>N/A | | | |
| Agreement vs. Correctness | Is quality also checked against control/gold instances or by manual inspection, since annotators can agree and still both be wrong? | Klie 2024, §3.3; Day 3 slides; group discussion | 1<br>2<br>3<br>N/A | | | |
| Case & Value Completeness | Does the dataset thoroughly cover domain edge cases, rare classes, and full feature values (with missing, corrupted, or incomplete attributes documented and quantified)? | group discussion | 1<br>2<br>3<br>N/A | | | |
| Agreement | Is at least one inter-annotator agreement measure used for the annotation or validation (not only the pilot study), and is it reported overall and per batch / per label? | Klie 2024, App. 2.4.3 & §3.3; Krippendorff 2004; Artstein and Poesio 2008; group discussion | 1<br>2<br>3<br>N/A | | | |
| Agreement Measure | Which measure is used: percent agreement, Cohen's κ, Fleiss' κ, Krippendorff's α (unitized), Pearson's r, Spearman's ρ, Kendall's τ, ICC, precision, recall, or F1? (Mark ? if unclear.) | Klie 2024, App. 2.8.1 | 1<br>2<br>3<br>N/A | | | |
| Metric Choice | Is the metric chance-corrected (not only percentage agreement), suited to the setup (2 annotators → Cohen's κ, more → Fleiss' κ, missing labels → Krippendorff's α), and are several metrics reported or the choice justified? | Klie 2024, §3.3; Day 3 slides; James 2026; own experiment (Task 3) | 1<br>2<br>3<br>N/A | | | |
| Agreement Value | What agreement value is reported for the final dataset (not the pilot)? (Use -1 if agreement is used but no value is given.) | Klie 2024, App. 2.8.2 | 1<br>2<br>3<br>N/A | | | |
| Label Distribution Reported | Is the label distribution (prevalence) reported? With skewed labels, S and AC1 are inflated and κ is deflated, so the value cannot be interpreted without it. | Own experiment (Task 2/3) | 1<br>2<br>3<br>N/A | | | |
| Agreement Inspection Size | On how many instances was agreement computed, and how large is the full dataset? (0 for both if the whole dataset.) | Klie 2024, App. 2.8.3 | 1<br>2<br>3<br>N/A | | | |
| IAA Setup & Uncertainty | Is it stated how many annotators labeled how many instances, whether all or only a subset was multiply annotated, and is an uncertainty estimate (e.g., confidence interval) given? | Klie 2024, §3.3; Chew et al. | 1<br>2<br>3<br>N/A | | | |
| Agreement Interpretation: Literature | Is the value interpreted using ranges from the literature (e.g., Landis and Koch 1977; Krippendorff 1980)? | Klie 2024, App. 2.8.4 | 1<br>2<br>3<br>N/A | | | |
| Agreement Interpretation: Custom | Does the paper claim a quality level such as sufficient, high, or good without citing any work, and is this justified for the domain? | Klie 2024, App. 2.8.4 | 1<br>2<br>3<br>N/A | | | |
| Agreement Interpretation: Compares to Previous | Does the paper compare its agreement to that of a similar, earlier dataset? | Klie 2024, App. 2.8.4 | 1<br>2<br>3<br>N/A | | | |
| Agreement Filter | Are instances filtered out if agreement is too low (e.g., a rolling threshold during annotation that flags low-consensus items or drifting annotators)? | Klie 2024, App. 2.4.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Manual Filter | Are instances filtered out manually (e.g., after inspecting low-agreement items)? | Klie 2024, App. 2.4.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Time Filter | Are instances filtered out because annotators annotated improbably quickly (e.g., minimum duration thresholds to discard "speeders")? | Klie 2024, App. 2.4.4; Ferracane et al. 2021; group discussion | 1<br>2<br>3<br>N/A | | | |
| Data Filtering (Post-Annotation) | Were ambiguous or low-quality annotated instances filtered out, and is the filtering justified and documented? | Klie 2024, §3.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Guideline Refinement | Were the guidelines or the scheme refined when they proved ambiguous or incomplete, were affected annotations revised, and is the quality of the final guidelines adequate? | Klie 2024, App. 2.4.4 & §3.4; group discussion | 1<br>2<br>3<br>N/A | | | |
| Overall Judgement | Considering all quality management performed and reported, is it excellent (iterative process, training, agreement and error rate, extensive validation, continuous human inspection), sufficient (some of these, at least some validation and manual inspection), or subpar (none of these; quality relies at most on aggregation)? | Klie 2024, App. 2.7 | 1<br>2<br>3<br>N/A | | | |


### Adjudication

| Criterion | Guiding Question | Source | Use Case Priority | Dataset 1 | Dataset 2 | Dataset 3 |
|---|---|---|---|---|---|---|
| Adjudication | Was adjudication (merging multiple annotations per instance into one) done only after sufficient quality was reached, and is the method stated? | Klie 2024, App. 2.5 & §3.5; group discussion | 1<br>2<br>3<br>N/A | | | |
| Majority Voting | Is the label assigned by at least half of the annotators chosen (or, as total agreement, only unanimous labels kept)? | Klie 2024, App. 2.5; Paun et al. 2018; group discussion | 1<br>2<br>3<br>N/A | | | |
| Manual Tie Breaking | Does a human inspect and curate instances that have no majority? | Klie 2024, App. 2.5; group discussion | 1<br>2<br>3<br>N/A | | | |
| Dawid-Skene | Is a probabilistic aggregation model of annotator expertise (Dawid-Skene) used? | Klie 2024, App. 2.5; Dawid and Skene 1979; group discussion | 1<br>2<br>3<br>N/A | | | |
| MACE | Is a probabilistic model of annotator expertise and spamming likelihood (MACE) used? | Klie 2024, App. 2.5; Hovy et al. 2013; group discussion | 1<br>2<br>3<br>N/A | | | |
| Manual Curation | Does a human manually inspect and curate instances? | Klie 2024, App. 2.5; Bareket and Tsarfaty 2021; group discussion | 1<br>2<br>3<br>N/A | | | |
| N/A | Is adjudication not applicable because there is only one annotation per instance or the task is text production? | Klie 2024, App. 2.5; group discussion | 1<br>2<br>3<br>N/A | | | |
| Unclear Adjudication | Is adjudication not mentioned although it must have happened (e.g., several annotations per instance)? | Klie 2024, App. 2.5; group discussion | 1<br>2<br>3<br>N/A | | | |
| Multiple Labels & Raw Data | Were multiple labels collected per instance, and are the raw (non-adjudicated) annotations published as well? | Klie 2024, §3.5; group discussion | 1<br>2<br>3<br>N/A | | | |
| Before vs. After Adjudication | Is it clear whether IAA was measured on independent annotations or after discussion/adjudication (which inflates agreement, e.g., our S rose from 0.83 to 0.95)? | Own experiment (Task 3); group discussion | 1<br>2<br>3<br>N/A | | | |
