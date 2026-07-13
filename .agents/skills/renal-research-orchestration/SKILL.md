---
name: renal-research-orchestration
description: Scaffold a governed, long-running renal therapeutics research loop after an upstream prioritization model has produced a ranked hypothesis. Use when coordinating clinical-evidence intake, cohort analysis, decision-pack generation, human review, and re-entry after new evidence. This skill defines workflow state and handoffs; it does not build, train, or replace the proprietary therapeutic prioritization model.
---

# Renal Research Orchestration

Define the handoffs for the post-prioritization research loop. This is **scaffolding**, not a deployed autonomous workflow.

## State machine

1. Accept a ranked research hypothesis from the upstream model.
2. Invoke `clinical-evidence-intake`; continue only when the evidence record is `ready`.
3. Invoke `renal-cohort-analysis` when cohort evidence is needed.
4. Invoke `evidence-decision-pack` to create the scientist-review artifact.
5. Record the human review result as `GO`, `HOLD`, or `NO-GO`.
6. On `GO` or `HOLD`, record the next evidence request and re-enter at intake when new evidence is available.
7. On `NO-GO`, preserve the decision pack and negative evidence; do not silently discard it.

## Required state

Use [the workflow state contract](references/workflow-state.md). Keep research state separate from patient-level data. Store only synthetic or approved governed references.

## Boundary

Do not claim that this scaffold trains a model, runs a clinical trial, accesses a provider system, or makes medical decisions. Require named human review before a decision changes program status.
