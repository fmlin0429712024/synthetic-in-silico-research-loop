---
name: renal-cohort-analysis
description: Design and summarize a synthetic or approved renal cohort evidence analysis for a drug-target-patient-subgroup hypothesis. Use when an evidence-intake record is ready and the task requires cohort definition, exposure and outcome logic, subgroup checks, missing-data review, and observational-study limitations. Do not use to claim causality, efficacy, or patient-specific treatment recommendations.
---

# Renal Cohort Analysis

Create an analysis plan and bounded evidence summary for a renal cohort.

## Workflow

1. Read the evidence-intake record and stop if it is not `ready`.
2. Define index date, inclusion/exclusion criteria, exposure, comparator, outcomes, follow-up window, and subgroup variables.
3. Identify likely confounders, missingness, censoring, and selection bias using [the analysis checklist](references/analysis-checklist.md).
4. Separate descriptive signals from causal claims.
5. Return a cohort-analysis record with assumptions, findings, and unresolved evidence gaps.

## Output

Return `cohort_analysis_record` with cohort logic, observed synthetic signal, subgroup consistency, limitations, and a `research_only` flag.

## Boundary

Use synthetic data in this repository. Do not issue patient-specific recommendations or state that observational evidence proves a medication effect.
