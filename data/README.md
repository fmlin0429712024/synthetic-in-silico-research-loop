# Synthetic Data

`research-program.json` is a fictional research program with a target, five candidate molecules, and synthetic evidence for the two selected candidates.

The evidence represents three downstream sources:

```text
assay / preclinical data + safety data + cohort-response data
                 ↓
      integrated evidence score
                 ↓
    revised candidate priority and next action
```

## Feedback-loop principle

Real wet-lab and clinical data do **not normally fine-tune AlphaFold**. They can instead:

- validate or reject a target/candidate hypothesis;
- improve a disease-, assay-, safety-, or patient-response model when appropriate data and governance exist;
- calibrate decision thresholds and determine the next experiment;
- create reusable organizational evidence for the next program.

This POC represents that feedback with deterministic synthetic values. It makes the decision loop visible without claiming biological truth.
