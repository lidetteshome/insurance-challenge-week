# Task 4: Risk-Based Premium Modeling and Prediction

This task focuses on building an end-to-end predictive system for dynamic insurance pricing using **risk-adjusted premiums**. The goal is to model:
- Probability of a claim (classification)
- Claim severity if a claim occurs (regression)
- Premium estimation using these components

---

## Goals

1. **Claim Probability Model**  
   - Target: `HasClaim` (binary)
   - Type: Classification
   - Metric: Accuracy, ROC AUC

2. **Claim Severity Model**  
   - Target: `TotalClaims` (only if > 0)
   - Type: Regression
   - Metrics: RMSE, R²

3. **Premium Estimation**  
   \[
   	ext{Premium} = 	ext{P(Claim)} 	imes 	ext{Predicted Severity} + 	ext{Expenses} + 	ext{Profit Margin}
   \]

---

## Pipeline Overview

1. Data Cleaning (drop/impute missing)
2. Feature Engineering (e.g., `VehicleAge`)
3. Encoding (One-hot / Label)
4. Train-Test Split (80:20)
5. Model Training (Logistic Regression, Random Forests, XGBoost)
6. Evaluation (Accuracy, RMSE, R²)
7. SHAP for Interpretability
8. Premium Derivation

---

## Outputs & Files

### Visuals
- `predicted_vs_actual_claims.png` – Severity model regression performance
- `shap_severity_summary.png` – SHAP global feature importance

### Artifacts
- `models/severity_model.pkl`
- `models/probability_model.pkl`
- `models/preprocessor.pkl`

### Scripts
```
notebooks/
└── task-4/
    └── modeling_pipeline.ipynb

scripts/
└── task-4/
    ├── modeling_utils.py
    ├── interpret_utils.py
    └── cli_predict.py
```

---

## CLI for Batch Prediction

You can predict risk-based premiums from a CSV file:

```bash
python scripts/task-4/cli_predict.py --data path/to/test_data.csv
```

Outputs include:
- Predicted claim probability
- Predicted severity
- Final risk-based premium

---

## SHAP Interpretability

We used SHAP to:
- Rank the top features for both models
- Interpret single predictions using force plots

> "SHAP analysis reveals that for every year older a vehicle is, the predicted claim amount increases by X Rand."

---

## Final Results

| Task | Model | Key Metric | Value |
|------|-------|------------|--------|
| Claim Probability | Logistic Regression | ROC AUC | High |
| Claim Severity | Random Forest | RMSE, R² | Solid |
| Premium | Derived | Dynamic | Personalized |

**Example**:  
- Claim Prob = 0.27  
- Claim Severity = ZAR 6,500  
- Premium = (0.27 × 6,500) + 500 = **ZAR 2,255**

---

## Deliverables Checklist

- [x] Data preprocessed
- [x] Classification & regression models trained
- [x] SHAP analysis complete
- [x] CLI prediction tool implemented
- [x] README finalized

---

**Author**: Lidet Teshome  
**Contact**: lidet.teshome.aastu@gmail.com  
