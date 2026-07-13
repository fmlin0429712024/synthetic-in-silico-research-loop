---
name: clinical-evidence-intake
description: Normalize and document a synthetic or approved clinical-evidence input for renal therapeutics research. Use when a ranked drug-target-patient-subgroup hypothesis needs clinical-trial or dialysis-provider data source metadata, provenance, permitted-use checks, and a consistent evidence package before analysis. Do not use to access PHI, make treatment recommendations, or infer clinical efficacy.
---

# Clinical Evidence Intake

Create a compact evidence-intake record before cohort or outcome analysis.

## Workflow

1. Confirm the input hypothesis: candidate, target/mechanism, intended patient subgroup, and research question.
2. Identify each evidence source as clinical-trial, care-delivery longitudinal, literature, or synthetic.
3. Record the source grain, time window, cohort definition, key fields, provenance, and permitted-use status.
4. Stop and flag the package if patient-identifying data is present in an unapproved location, if use permission is unclear, or if provenance is missing.
5. Produce an intake record using the fields in [the evidence contract](references/evidence-contract.md).

## Output

Return an `evidence_intake_record` with source inventory, limitations, and a readiness state of `ready`, `needs-clarification`, or `blocked`.

## Boundary

Treat clinical-trial data and dialysis-provider longitudinal data as separate sources. Do not merge them silently. Do not claim causal effect, medication efficacy, or a treatment recommendation.
