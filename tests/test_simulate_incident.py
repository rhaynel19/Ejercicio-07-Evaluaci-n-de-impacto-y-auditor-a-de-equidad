import json

import pytest
import yaml

from scripts.simulate_incident import simulate_incident


def test_simulate_incident_writes_explicit_synthetic_exercise(tmp_path):
    metrics_path = tmp_path / "metrics.json"
    metrics_path.write_text(
        json.dumps({"differences": {"recall": 0.3}}),
        encoding="utf-8",
    )
    config_path = tmp_path / "governance.yml"
    config_path.write_text(
        yaml.safe_dump({"gates": {"max_recall_gap": 0.16}}),
        encoding="utf-8",
    )
    output_path = tmp_path / "reports" / "postmortem.md"

    result = simulate_incident(metrics_path, config_path, output_path)

    report = result.read_text(encoding="utf-8")
    assert result == output_path
    assert "escenario simulado" in report
    assert "no registra un incidente real" in report
    assert "Responsable institucional: sin designar" in report
    assert "0.300" in report


def test_simulate_incident_rejects_non_breaching_metrics(tmp_path):
    metrics_path = tmp_path / "metrics.json"
    metrics_path.write_text(
        json.dumps({"differences": {"recall": 0.1}}),
        encoding="utf-8",
    )
    config_path = tmp_path / "governance.yml"
    config_path.write_text(
        yaml.safe_dump({"gates": {"max_recall_gap": 0.16}}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="No recall-gap incident to simulate"):
        simulate_incident(metrics_path, config_path, tmp_path / "postmortem.md")
