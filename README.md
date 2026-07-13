# Synthetic In-Silico Research Loop

A small **dry-lab** POC for an AI-supported scientific decision loop.

```text
research question → candidate prioritization → simulated evidence
→ transparent GO / HOLD / NO-GO decision → next iteration
```

All targets, molecules, lab results, cohort signals, and decisions are synthetic. This is educational software—not medical software or biological validation.

## What it demonstrates

- AI can prioritize which hypotheses deserve scarce experiments.
- Lab and clinical evidence can update the **next research decision**.
- A human scientist remains responsible for review and real-world validation.

See [the pipeline map](docs/PIPELINE.md) and [synthetic-data note](data/README.md).

## Run

```bash
python3 src/closed_loop.py
```

It creates a local, ignored decision report in `outputs/`.
