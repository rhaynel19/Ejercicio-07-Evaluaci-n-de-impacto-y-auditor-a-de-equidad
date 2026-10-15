import pandas as pd

REQUIRED_IMPACT={"purpose","assisted_decision","users","affected_population","owner","non_predictive_alternative","out_of_scope_use","withdrawal_condition","appeal_mechanism"}
REQUIRED_RISK={"id","scenario","affected","likelihood_1_4","impact_1_4","control","owner","evidence","residual"}

def validate_impact(data):
    missing=REQUIRED_IMPACT-set(data)
    incomplete=[k for k in REQUIRED_IMPACT if str(data.get(k,"" )).strip() in {"","REPLACE"}]
    if missing or incomplete: raise ValueError(f"Incomplete impact assessment: {sorted(missing|set(incomplete))}")
    return True

def score_risks(df):
    if REQUIRED_RISK-set(df.columns): raise ValueError("Risk register columns missing")
    if df.empty: raise ValueError("Risk register must contain at least one risk")
    text_cols=["id","scenario","affected","control","owner","evidence","residual"]
    text=df[text_cols].fillna("").astype(str).apply(lambda column: column.str.strip())
    if text.eq("").any().any() or text.apply(lambda column: column.str.upper().eq("REPLACE")).any().any():
        raise ValueError("Complete all risk fields")
    if text["id"].duplicated().any():
        raise ValueError("Risk identifiers must be unique")
    residual=text["residual"].str.lower()
    if not residual.isin({"low","medium","high"}).all():
        raise ValueError("Residual risk must be low, medium, or high")
    for column in ["likelihood_1_4","impact_1_4"]:
        values=pd.to_numeric(df[column],errors="coerce")
        if values.isna().any() or not values.between(1,4).all() or not values.mod(1).eq(0).all():
            raise ValueError(f"{column} must contain integers from 1 to 4")
    out=df.copy(); out["priority"]=out.likelihood_1_4.astype(int)*out.impact_1_4.astype(int)
    return out.sort_values(["priority","impact_1_4"],ascending=False)
