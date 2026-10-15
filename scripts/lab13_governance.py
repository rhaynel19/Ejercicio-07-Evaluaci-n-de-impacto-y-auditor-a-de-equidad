import json
from pathlib import Path

import pandas as pd
import yaml

from inf8239_u04.data import load_data
from inf8239_u04.governance import load_config, validate_raci
from inf8239_u04.pipeline import run

cfg=load_config(); validate_raci(pd.read_csv("student_inputs/raci.csv")); result=run(load_data(),cfg["gates"])
human_decision=yaml.safe_load(Path("student_inputs/lab12_decision.yml").read_text(encoding="utf-8"))
out=Path("reports/lab13"); out.mkdir(parents=True,exist_ok=True)
(out/"deployment_decision.json").write_text(json.dumps({
    "metrics":result["metrics"],
    "gaps":result["gaps"],
    "resources":result["resources"],
    "decision":result["decision"],
    "human_decision":{
        "status":human_decision["decision_status"],
        "recommendation":human_decision["recommendation"],
        "scope":"Synthetic educational use only; no operational use with real people.",
    },
},indent=2),encoding="utf-8")
result["by_group"].to_csv(out/"fairness_by_group.csv"); print(result["decision"])
