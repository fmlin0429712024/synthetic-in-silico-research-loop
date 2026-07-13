"""Synthetic, deterministic AI-scientist decision-loop demo. Not medical software."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "research-program.json"
OUTPUT_FILE = ROOT / "outputs" / "decision-report.json"


def prior_score(candidate):
    """Transparent upstream prioritization; production systems need scientific review."""
    return round(
        0.55 * candidate["computational_fit"]
        + 0.30 * candidate["developability"]
        + 0.15 * candidate["novelty"],
        3,
    )


def evidence_score(evidence):
    """Synthetic evidence integration across experimental and translational signals."""
    return round(
        0.30 * evidence["assay_effect"]
        + 0.25 * evidence["preclinical_signal"]
        + 0.25 * evidence["safety_signal"]
        + 0.12 * evidence["cohort_response"]
        + 0.08 * evidence["subgroup_consistency"],
        3,
    )


def recommendation(score):
    if score >= 0.78:
        return "GO: request scientist review and design the next real validation study"
    if score >= 0.68:
        return "HOLD: collect a targeted follow-up experiment before advancing"
    return "NO-GO: deprioritize in this synthetic program"


def main():
    program = json.loads(DATA_FILE.read_text())
    ranked = sorted(
        ({**candidate, "prior_score": prior_score(candidate)} for candidate in program["candidates"]),
        key=lambda item: item["prior_score"],
        reverse=True,
    )
    selected = ranked[:2]
    decisions = []

    for candidate in selected:
        evidence = program["simulated_evidence"][candidate["id"]]
        integrated_score = evidence_score(evidence)
        final_score = round(0.35 * candidate["prior_score"] + 0.65 * integrated_score, 3)
        decisions.append({
            "candidate_id": candidate["id"],
            "upstream_prior_score": candidate["prior_score"],
            "simulated_evidence": evidence,
            "integrated_evidence_score": integrated_score,
            "updated_decision_score": final_score,
            "recommendation": recommendation(final_score),
            "human_review_required": True,
        })

    report = {
        "program_id": program["program_id"],
        "disclaimer": program["disclaimer"],
        "target_hypothesis": program["target"]["hypothesis"],
        "trace": [
            "Ranked synthetic candidates from prior computational evidence.",
            "Selected the top two candidates for simulated downstream evidence.",
            "Integrated synthetic assay, preclinical, safety, and cohort-response signals.",
            "Generated a transparent, human-review-required next decision.",
        ],
        "initial_ranking": [{"candidate_id": item["id"], "score": item["prior_score"]} for item in ranked],
        "decisions": sorted(decisions, key=lambda item: item["updated_decision_score"], reverse=True),
    }
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Created {OUTPUT_FILE.relative_to(ROOT)}")
    for item in report["decisions"]:
        print(f"{item['candidate_id']}: {item['updated_decision_score']} — {item['recommendation']}")


if __name__ == "__main__":
    main()
