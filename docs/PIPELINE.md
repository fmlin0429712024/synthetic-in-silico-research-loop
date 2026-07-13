# Pipeline Map

```text
Disease question
  ↓
Target hypothesis
  ↓
In-silico candidate prioritization
  ├─ Protein structure / interaction hypothesis: AlphaFold-type models
  ├─ Molecule ranking: docking, chemistry models, literature, prior data
  └─ POC: transparent synthetic scoring rule
  ↓
Wet-lab and preclinical evidence
  └─ POC: simulated assay, efficacy, and safety signals
  ↓
Clinical / translational evidence
  └─ POC: simulated cohort response and subgroup consistency
  ↓
Evidence integration + scientist review
  ↓
GO / HOLD / NO-GO → next target, candidate, or experiment iteration
```

## Real-world mapping

| POC step | Real technology or product category |
|---|---|
| Structure / interaction hypothesis | AlphaFold-type structure and interaction models |
| Candidate prioritization | Docking, virtual screening, chemistry models, scientific literature search |
| Experimental evidence | ELN/LIMS, assay platforms, CRO outputs, biomarker systems |
| Clinical evidence | Governed trial, patient, and biomarker data systems |
| Research orchestration | AI scientist / agent platform, data connectors, provenance, evaluation, human review |

AlphaFold is one upstream capability. It helps formulate structural and interaction hypotheses; it does not itself prove efficacy, replace wet-lab work, or make clinical decisions.
