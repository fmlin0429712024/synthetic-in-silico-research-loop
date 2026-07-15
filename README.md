# Healthcare Agentic AI POC — Drug Discovery Research Loop

## RTRO — Renal Therapeutics Research Orchestrator

A synthetic dry-lab POC for an AI-orchestrated renal therapeutics research pipeline. It connects upstream discovery and drug-repurposing hypotheses with downstream clinical evidence and iterative research decisions.

RTRO demonstrates the closed-loop AI science pattern:

> use computation to prioritize a research hypothesis, use experimental evidence to test it, then use the evidence to make the next decision better.

It demonstrates the orchestration and decision layer behind an AI-scientist platform. It does **not** claim biological validation, treatment recommendation, or clinical efficacy.

## 1. Research system context — the full evidence loop

This diagram explains the **entire research system**. It includes upstream scientific tools and the long clinical-evidence flywheel. RTRO does not implement the upstream model or real trials; it makes the downstream evidence and workflow layer concrete.

```mermaid
flowchart TD
    Q[Renal research question] --> H[Target / mechanism hypothesis]
    H --> S[Upstream scientific tools<br/>AlphaFold-type models + docking + literature]
    S --> C[Discovery or repurposing candidate hypotheses]
    C --> M[Specialized therapeutic prioritization model<br/>gray-box in this POC]
    M --> V[Design clinical validation study]
    V --> T[Clinical-trial data<br/>efficacy, safety, biomarkers]
    P[Dialysis-provider data asset<br/>longitudinal patient records and outcomes<br/>DaVita-domain experience; synthetic proxy in this POC] --> E
    T --> E[Clinical evidence integration]
    H1[Historical trial / literature evidence] --> E
    E --> M
    M --> D{Scientist-reviewed decision}
    D -->|GO| V
    D -->|HOLD| E
    D -->|NO-GO| X[Preserve negative evidence]

    classDef upstream fill:#dbeafe,stroke:#2563eb,color:#111827;
    classDef data fill:#dcfce7,stroke:#16a34a,color:#111827;
    classDef model fill:#e5e7eb,stroke:#4b5563,color:#111827;
    class S upstream;
    class P,T,H1,E data;
    class M model;
```

## Why this matters

Renal research is a sequence of expensive, uncertain decisions. The value of AI is not to eliminate wet labs or clinical studies. It is to reduce uncertainty before each investment, connect fragmented evidence, and make the next experiment more purposeful.

## What this POC contains

| Layer | In this POC | Real-world equivalent |
|---|---|---|
| Research context | Fictional renal therapeutic hypothesis and target | Renal research question, literature, internal program context |
| Upstream reasoning | Transparent discovery / repurposing candidate ranking | Structure/interaction models, docking, chemistry models, literature and data analysis |
| Evidence | Synthetic clinical-trial-like and dialysis-provider cohort signals | Historical trial evidence, biomarkers, and governed longitudinal patient data |
| Decision | Traceable `GO` / `HOLD` / `NO-GO` | Scientist-reviewed experiment and program decisions |
| Learning loop | Revised score and next action | New hypotheses, experiment designs, specialized model improvement, organizational knowledge |

## 2. Skills orchestration — the RTRO delivery layer

This is intentionally **not a second copy of the full pipeline**. It begins after the upstream model has produced a ranked research hypothesis. It shows the concrete, post-prioritization workflow that an FDE / agent-delivery team can implement and govern.

```mermaid
flowchart TD
    A[Ranked research hypothesis<br/>from upstream prioritization model] --> E[renal-research-orchestration<br/>scaffolding]
    E --> B[clinical-evidence-intake<br/>short-running]
    B --> C[renal-cohort-analysis<br/>short-running]
    C --> D[evidence-decision-pack<br/>short-running]
    D --> F{Scientist review}
    F -->|GO| G[Design next clinical validation]
    G --> H[New trial / care-delivery evidence]
    H --> E
    F -->|HOLD| E
    F -->|NO-GO| I[Preserve negative evidence]

    classDef short fill:#dcfce7,stroke:#16a34a,color:#111827;
    classDef scaffold fill:#e5e7eb,stroke:#4b5563,color:#111827;
    class B,C,D short;
    class E scaffold;
```

| Skill | Role |
|---|---|
| `renal-research-orchestration` | Long-running workflow **scaffold**: state, handoffs, re-entry conditions |
| `clinical-evidence-intake` | Short-running: source metadata, provenance, and governance checks |
| `renal-cohort-analysis` | Short-running: cohort, subgroup, and observational-evidence analysis plan |
| `evidence-decision-pack` | Short-running: traceable scientist-review artifact |

The skills do not build or retrain the proprietary model, access real patient data, or make medical decisions. They prototype the governed evidence workflow around the model.

## Scientific boundary

All targets, molecules, lab results, cohort signals, and decisions are synthetic. This repository is educational software—not medical software.

- It does not run AlphaFold, docking, molecular dynamics, wet-lab experiments, animal studies, or clinical trials.
- Wet-lab and animal studies are deliberately abstracted out of this POC; the synthetic clinical-evidence layer represents the downstream evidence and feedback loop.
- AlphaFold-type models belong in the upstream structural-hypothesis layer; they do not prove efficacy or replace validation.
- Wet-lab and clinical evidence normally improves scientific decisions, disease/response models, and future experiment selection—not automatically AlphaFold itself.
- Every meaningful real-world decision requires scientist review, data governance, and regulated validation.
- Real DaVita or other patient data is **not** included and must never be placed in this public repository.

## Supporting detail

- [End-to-end pipeline, orchestration, and technology map](docs/PIPELINE.md)
- [Synthetic data model and feedback loop](data/README.md)
- [Skills implementation notes](docs/SKILLS_WORKFLOW.md)
- [Repo-scoped skill folders](.agents/skills/)

## Run locally

```bash
python3 src/closed_loop.py
```

The script generates a local, ignored decision report in `outputs/`.
