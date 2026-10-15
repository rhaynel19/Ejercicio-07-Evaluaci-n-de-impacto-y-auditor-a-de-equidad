import json
from datetime import UTC, datetime
from pathlib import Path

import yaml


def simulate_incident(
    metrics_path="reports/lab12/tree/global_metrics.json",
    config_path="configs/governance.yml",
    output_path="reports/lab13/INCIDENT_POSTMORTEM.md",
):
    metrics_file = Path(metrics_path)
    config_file = Path(config_path)
    if not metrics_file.is_file():
        raise FileNotFoundError(f"Run the tree audit first: {metrics_file}")
    if not config_file.is_file():
        raise FileNotFoundError(f"Governance configuration not found: {config_file}")

    metrics = json.loads(metrics_file.read_text(encoding="utf-8"))
    config = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    try:
        recall_gap = float(metrics["differences"]["recall"])
        max_recall_gap = float(config["gates"]["max_recall_gap"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(
            "Metrics or governance config is missing a valid recall-gap gate"
        ) from exc

    if recall_gap <= max_recall_gap:
        raise ValueError(
            f"No recall-gap incident to simulate: {recall_gap:.3f} "
            f"does not exceed {max_recall_gap:.3f}"
        )

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    detected_at = datetime.now(UTC).isoformat()
    report = f"""# Simulación de incidente (ejercicio de mesa)

Este documento describe un escenario simulado; no registra un incidente real ni
una notificación enviada a personas.

- Marca temporal de la simulación (UTC): {detected_at}
- Señal: el modelo tree registró una brecha de recall de {recall_gap:.3f}, por encima del umbral configurado de {max_recall_gap:.3f}.
- Clasificación: fallo de puerta de equidad en una prueba con datos sintéticos.
- Contención recomendada: no usar el modelo para uso operacional; volver a revisión manual sin puntuación.
- Evidencia: `{metrics_file.as_posix()}` y `{config_file.as_posix()}`.
- Comunicación: ninguna enviada; el escenario es exclusivamente académico y no contiene personas reales.
- Acción correctiva: revisar la causa de la brecha, repetir auditorías globales y por grupo y mantener suspendido el apoyo del modelo hasta que se aprueben los controles.
- Responsable institucional: sin designar; asignar antes de cualquier uso operacional.
- Estado: simulación completada; aprobación de reanudación no aplica.
"""
    output.write_text(report, encoding="utf-8")
    return output


if __name__ == "__main__":
    print(simulate_incident())
