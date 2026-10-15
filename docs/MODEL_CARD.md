# Model Card — Territorial Review DSS (synthetic)

## Intended use
Educational evaluation of a model that ranks synthetic cases for human review. The author-selected exercise decision limits the system to human-review prioritization and prohibits operational use with real people.

## Out-of-scope use
Automatic intervention, eligibility decisions, emergency declarations, and profiling or inference about real populations. These restrictions also appear in `configs/governance.yml` and the synthetic Dataset Card.

## Data and split
The dataset is explicitly synthetic and educational. Rows are sorted by `received_date`; the first 75% are used for training and the final 25% for testing (`temporal_split`, no shuffle). The test set contains 160 synthetic rows. Model inputs are `zone`, `age_band`, `previous_incidents`, `infrastructure_score`, and `exposure`. Protected group and age band are used to audit outcomes. Direct identifiers are prohibited by schema validation.

## Global and subgroup evaluation
On the temporal test set:

| Model | Accuracy | Recall | Recall gap | FPR gap | Group FPR (G1/G2) |
|---|---:|---:|---:|---:|---:|
| Logistic regression | 0.719 | 0.717 | 0.138 | 0.125 | 0.250 / 0.375 |
| Decision tree | 0.706 | 0.717 | 0.181 | 0.168 | 0.269 / 0.438 |

The configured gates require recall >= 0.68, recall gap <= 0.16, and FPR gap <= 0.16. The logistic model passes the configured gates; the decision tree exceeds the configured disparity limits. Intersections of protected group and age band include cells as small as 8 records. These results are descriptive of synthetic data only, with no external validity or uncertainty intervals.

## Green AI evidence
In the recorded run, logistic training took approximately 0.229 seconds and the serialized model was 3.56 KB; the tree took approximately 0.058 seconds and was 7.87 KB. LAB13 measured logistic inference latency at approximately 0.052 ms per test record. Training and latency values are single-run measurements, hardware-dependent, and do not establish environmental impact or production performance.

## Limitations, human oversight and appeal
Synthetic data cannot establish performance, fairness, or safety for a real population. The model must not make decisions about people. Human review and an appeal/correction path are required controls for any future proposal, but no operational appeal process or responsible institution has been assigned in this exercise. A future real-world proposal requires appropriate data, uncertainty analysis, external validation, stakeholder participation, legal review, and approved controls.

## Owner and review date
Academic author: Edwin Ramón José Nolasco. No institutional or operational owner has been designated. Review date for these recorded outputs: 2026-10-14. Update the card if code, data, gates, or decision changes.
