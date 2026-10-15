from pathlib import Path

import yaml

decision = yaml.safe_load(
    Path("student_inputs/lab12_decision.yml").read_text(encoding="utf-8")
)
if not isinstance(decision, dict):
    raise TypeError("Decision record must be a YAML mapping")

missing = [
    key
    for key, value in decision.items()
    if value is None or str(value).strip() in {"", "REPLACE"}
]
if missing:
    raise ValueError(f"Complete: {missing}")

if decision.get("decision_status") not in {"GO", "REVIEW", "STOP"}:
    raise ValueError("decision_status must be GO, REVIEW, or STOP")

print(f"decision_status: {decision['decision_status']}")
