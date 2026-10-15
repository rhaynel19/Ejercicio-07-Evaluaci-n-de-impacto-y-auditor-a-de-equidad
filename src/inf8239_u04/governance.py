from pathlib import Path

import yaml


def load_config(path="configs/governance.yml"):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))

def validate_raci(df):
    required={"activity","R","A","C","I"}
    if required-set(df.columns): raise ValueError("RACI columns missing")
    if df.empty: raise ValueError("RACI must contain at least one activity")
    assignments=df[["activity","R","A","C","I"]].fillna("").astype(str).apply(lambda s:s.str.strip())
    if assignments.eq("").any().any(): raise ValueError("Every activity needs a name and R, A, C, and I assignments")
    if assignments["activity"].duplicated().any(): raise ValueError("RACI activities must be unique")
    return True

def deployment_decision(metrics, gaps, resources, gates):
    checks={
      "recall": metrics["recall"] >= gates["min_recall"],
      "recall_gap": gaps["recall_gap"] <= gates["max_recall_gap"],
      "fpr_gap": gaps["fpr_gap"] <= gates["max_fpr_gap"],
      "latency": resources["latency_ms"] <= gates["max_latency_ms"],
      "model_size": resources["model_kb"] <= gates["max_model_kb"],
    }
    failed=[k for k,v in checks.items() if not v]
    return {"status":"GO" if not failed else "REVIEW", "checks":checks, "failed":failed, "human_action":"Document review and final decision"}
