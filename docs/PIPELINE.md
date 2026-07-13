# RTRO Research Pipeline

## The real pipeline

```mermaid
flowchart TD
    A[1. Renal research question] --> B[2. Target / mechanism hypothesis]
    B --> C[3. Upstream scientific tools<br/>AlphaFold-type models, docking, literature]
    C --> D[4. Discovery or repurposing candidate hypotheses]
    D --> E[5. Specialized therapeutic prioritization model]
    T[Historical clinical-trial evidence] --> E
    P[Dialysis-provider longitudinal patient evidence] --> E
    E --> G[6. Evidence integration and scientist review]
    G --> H{GO / HOLD / NO-GO}
    H -->|Advance| I[7. Design next validation study]
    I --> N[New clinical-study evidence]
    N --> E
    H -->|Learn more| E
    H -->|Stop| J[Preserve negative evidence]
```

The real pipeline can include wet-lab and animal/preclinical studies between candidate prioritization and clinical work. RTRO deliberately abstracts those stages to keep the POC focused on the orchestration and clinical-evidence feedback loop. The POC compresses the remaining pipeline into minutes by using synthetic data only.

## Technology map

| Stage | Question | Typical AI / data capability | POC representation |
|---|---|---|---|
| 1–2 | What renal mechanism or unmet need is worth investigating? | Literature, omics, experimental and clinical evidence synthesis | Fictional ESKD research question and target hypothesis |
| 3 | Which new or existing drug might plausibly affect the target or mechanism? | Protein structure/interaction models such as AlphaFold-type models; generative chemistry | Fixed fictional candidate pool |
| 4 | Which hypothesis should receive scarce resources first? | Docking, virtual screening, chemistry/developability models, prior evidence | Transparent initial score |
| 5 | How should candidate, patient, and historical trial evidence be combined? | Specialized/proprietary prioritization model, statistical models, rules, agent orchestration, provenance | Deterministic evidence-integration model |
| 6 | Is there evidence across renal patient subgroups or biomarkers? | Governed clinical/biomarker data analysis, patient stratification | Synthetic trial-like and dialysis-provider cohort signals |
| 7 | What should happen next? | Evaluation, human review, prospective-study design | Traceable score and `GO` / `HOLD` / `NO-GO` |

## Where AlphaFold fits

AlphaFold-type models are an important **upstream** capability. They predict protein structure and, in newer interaction-oriented approaches, support hypotheses about protein–molecule or protein–protein interactions. In RTRO, they provide one source of evidence before the specialized therapeutic prioritization model; they can support new-discovery or existing-drug repurposing hypotheses when a credible molecular target exists. They do not independently choose a drug, prove an effect in a living system, or replace clinical validation.

## What the loop learns

```mermaid
flowchart LR
    X[Historical or new clinical evidence] --> Y[Validate or reject hypothesis]
    Y --> Z[Update candidate priority]
    Z --> AA[Choose next validation study]
    AA --> X
    Y --> AB[Improve disease, assay, safety, or response models when appropriate]
```

The feedback is not automatically “fine-tune AlphaFold with clinical data.” AlphaFold-type tools supply upstream structure information. The loop feeds the **specialized therapeutic prioritization model**: a potential proprietary system combining evidence-integration logic, statistical models, evaluation, and scientist-defined rules. Different data types can improve different components; the common outcome is better scientific prioritization and a more defensible next decision.
