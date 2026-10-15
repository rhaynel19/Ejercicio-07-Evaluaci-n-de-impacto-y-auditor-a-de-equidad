
import json
from pathlib import Path

import pandas as pd
import yaml

from inf8239_u04.impact import score_risks, validate_impact

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
if not isinstance(decision, dict):
    raise TypeError("Decision record must be a YAML mapping")
missing_decision = [
    key
    for key, value in decision.items()
    if value is None or str(value).strip() in {"", "REPLACE"}
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
        "next_step": "Ejecutar scripts/lab12_audit.py --model logistic",
    }

(out / "rmf_summary.json").write_text(
    json.dumps(
        {
            "GOVERN": {
                "academic_owner": impact["owner"],
                "institutional_owner": "sin designar",
                "prohibited_uses": [
                    "intervención automática",
                    "decisiones de elegibilidad",
                    "declaración de emergencia",
                    "uso operacional con personas reales",
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

governance_path = Path("reports/lab13/deployment_decision.json")
if governance_path.is_file():
    governance_result = json.loads(governance_path.read_text(encoding="utf-8"))
    technical_status = governance_result["decision"]["status"]
else:
    technical_status = "pendiente"

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

## Decisión y autorización

- Puertas técnicas de LAB13: {technical_status}. Este estado solo compara métricas con umbrales configurados; no autoriza despliegue.
- Estado para uso operacional con personas reales: {decision["decision_status"]}.
- Alcance del ejercicio: {decision["recommendation"]}
- Alternativa sin modelo: {impact["non_predictive_alternative"]}
- Incertidumbre: datos sintéticos; sin validación externa ni intervalos de confianza; celdas interseccionales pequeñas; no hubo consulta a personas afectadas.
- Condición de retiro: {impact["withdrawal_condition"]}

## Priorización de riesgos

La probabilidad y el impacto son valoraciones cualitativas provisionales de 1
a 4; la prioridad es su producto, no una probabilidad estimada empíricamente.
Los niveles residuales son juicios cualitativos y requieren revisión del autor
y de la institución antes de cualquier uso operacional.

| Riesgo | Prioridad inherente | Nivel residual | Responsable |
|---|---:|---|---|
{risk_lines}

La decisión STOP aplica al uso operacional con personas reales; el trabajo puede
continuar únicamente como ejercicio académico con datos sintéticos y supervisión
humana. Si una propuesta futura incumple un umbral configurado, carece de
evidencia representativa o controles aprobados, o se sale del alcance, se debe
suspender la priorización asistida y usar la alternativa manual no predictiva.
"""

(out / "DECISION_RECORD.md").write_text(
    decision_record,
    encoding="utf-8",
)

print(risks[["id", "priority", "owner"]].head(3).to_string(index=False))
