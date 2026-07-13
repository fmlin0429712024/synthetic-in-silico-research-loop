# Evidence Intake Contract

Create one record per source with these fields:

```text
source_id
source_type: synthetic | clinical_trial | care_delivery | literature
allowed_use: synthetic_demo | approved_research | unknown
data_grain: patient | encounter | treatment | trial_participant | aggregate
time_window
cohort_definition
key_fields
provenance
known_limitations
```

Use `blocked` when `allowed_use` is unknown or the requested output could expose patient-identifying information.
