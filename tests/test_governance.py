import pandas as pd
import pytest

from inf8239_u04.governance import deployment_decision, validate_raci


def test_failed_gate_requires_review():
    d=deployment_decision({"recall":.5},{"recall_gap":.1,"fpr_gap":.1},{"latency_ms":1,"model_kb":5},{"min_recall":.7,"max_recall_gap":.2,"max_fpr_gap":.2,"max_latency_ms":10,"max_model_kb":20}); assert d["status"]=="REVIEW"


def test_raci_requires_accountable():
    with pytest.raises(ValueError): validate_raci(pd.DataFrame([{"activity":"deploy","R":"ML","A":"","C":"DS","I":"Users"}]))


def test_raci_rejects_empty_table():
    with pytest.raises(ValueError, match="at least one activity"):
        validate_raci(pd.DataFrame(columns=["activity", "R", "A", "C", "I"]))


def test_raci_rejects_duplicate_activities():
    row = {"activity": "deploy", "R": "ML", "A": "DS", "C": "Ops", "I": "Users"}
    with pytest.raises(ValueError, match="must be unique"):
        validate_raci(pd.DataFrame([row, row]))
