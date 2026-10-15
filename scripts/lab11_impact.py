
import json
from pathlib import Path

import pandas as pd
import yaml

from inf8239_u04.impact import validate_impact, score_risks

out = Path("reports/lab11")
out.mkdir(parents=True, exist_ok=True)

impact = yaml.safe_load(
    Path("student_inputs/lab11_impact.yml").read_text(encoding="utf-8")
)
validate_impact(impact)

stake = pd.read_csv("student_inputs/stakeholders.csv")

if stake.astype(str).apply(lambda s: s.str.contains("REPLACE")).any().any():
    raise ValueError("Complete stakeholders.csv")
if stake[["stakeholder", "benefit", "harm", "power", "participation"]].fillna("").eq("").any().any():
    raise ValueError("Stakeholder assessment contains blank fields")

risks = score_risks(
    pd.read_csv("student_inputs/risk_register.csv")
)

risks.to_csv(out / "risk_register_scored.csv", index=False)
stake.to_csv(out / "stakeholders.csv", index=False)

decision = yaml.safe_load(
    Path("student_inputs/lab12_decision.yml").read_text(encoding="utf-8")
)
missing_decision = [
    key
    for key, value in decision.items()
    if str(value).strip() in {"", "REPLACE"}
]
if missing_decision:
    raise ValueError(f"Complete lab12_decision.yml: {missing_decision}")

metrics_path = Path("reports/lab12/logistic/global_metrics.json")
if metrics_path.exists():
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    measure_summary = {
        "status": "completada",
        "model": "logistic",
        "metrics": metrics["metrics"],
        "differences": metrics["differences"],
    }
else:
    measure_summary = {
        "status": "pendiente",
        "next_step": "Run scripts/lab12_audit.py --model logistic",
    }

(out / "rmf_summary.json").write_text(
    json.dumps(
        {
            "GOVERN": {
                "academic_owner": impact["owner"],
                "institutional_owner": "not designated",
                "prohibited_uses": [
                    "automatic intervention",
                    "eligibility decision",
                    "emergency declaration",
                    "operational use with real people",
                ],
            },
            "MAP": {
                "purpose": impact["purpose"],
                "assisted_decision": impact["assisted_decision"],
                "risk_count": len(risks),
                "risk_scale": "probabilidad e impacto cualitativos provisionales, cada uno de 1 a 4",
            },
            "MEASURE": measure_summary,
            "MANAGE": {
                "recommendation": decision["recommendation"],
                "withdrawal_condition": impact["withdrawal_condition"],
                "appeal_mechanism": impact["appeal_mechanism"],
                "institutional_owner": "sin designar",
            },
        },
        indent=2,
    ),
    encoding="utf-8",
)

risk_lines = "\n".join(
    f"| {row.id} | {row.priority} | {row.residual} | {row.owner} |"
    for row in risks.itertuples(index=False)
)
decision_record = f"""# Registro de decisión — U04.E07

## Alcance y responsables

- Propósito: {impact["purpose"]}
- Responsable académico: {impact["owner"]}
- Responsable institucional/operacional: sin designar; el uso operacional no está autorizado.
- Decisión asistida: {impact["assisted_decision"]}
- Daño prioritario seleccionado por el autor: {decision["priority_harm"]}

## Evidencia y umbrales

- Métrica principal y tolerancias: {decision["primary_metric"]}; {decision["tolerance"]}
- Artefactos de evidencia: {decision["evidence"]}
- Estado de medición: {measure_summary["status"]}
- Limitación: {decision["limitation"]}

## Priorización de riesgos

La probabilidad y el impacto son valoraciones cualitativas provisionales de 1
a 4; la prioridad es su producto, no una probabilidad estimada empíricamente.
Los niveles residuales son juicios cualitativos y requieren revisión del autor
y de la institución antes de cualquier uso operacional.

| Riesgo | Prioridad inherente | Nivel residual | Responsable |
|---|---:|---|---|
{risk_lines}

## Decisión

{decision["recommendation"]}

Esta es la decisión restrictiva del autor para el ejercicio y no autoriza
despliegue. Si una propuesta futura incumple un umbral configurado, carece de
evidencia representativa o controles aprobados, o se sale del alcance, se debe
suspender la priorización asistida y usar la alternativa manual no predictiva.
"""

(out / "DECISION_RECORD.md").write_text(
    decision_record,
    encoding="utf-8",
)

print(risks[["id", "priority", "owner"]].head(3).to_string(index=False))
