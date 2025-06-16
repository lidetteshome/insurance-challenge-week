
# Task 4 - Risk-Based Premium Modeling and Prediction

## 🎯 Objectives

Develop models to predict:
1. **Claim Severity** – estimate cost of a claim when it occurs
2. **Premium Optimization** – align premium predictions with expected risk
3. **Probability of Claim** *(Advanced)* – classify if a claim will occur

## 🧪 Targets and Metrics

| Task | Target | Type | Metrics |
|------|--------|------|---------|
| Claim Severity | TotalClaims (if > 0) | Regression | RMSE, R² |
| Premium | CalculatedPremiumPerTerm | Regression | RMSE, MAE, R² |
| Probability of Claim | TotalClaims > 0 | Classification | Accuracy, ROC AUC, F1 |

## 🛠️ Pipeline Overview

1. **Data Cleaning** – drop/impute nulls
2. **Feature Engineering** – derive new ratios or encodings
3. **Encoding** – one-hot or label encoding
4. **Split** – 80:20 train-test
5. **Models** – LinearRegression, RandomForest, XGBoost (for both regression and classification)
6. **Evaluation** – compare metrics across models
7. **Interpretation** – SHAP for explainability
8. **Risk-Based Premium** – Calculated as:
   \[ \text{Premium} = \text{P(Claim)} \times \text{Predicted Severity} + \text{Expenses} + \text{Profit Margin} \]

## 🗂️ File Structure

```
notebooks/
└── task-4/
    └── modeling_pipeline.ipynb

scripts/
├── task-4/
│   ├── modeling_utils.py
│   ├── interpret_utils.py
│   └── cli_predict.py  # CLI tool to serve predictions
```

## 📈 SHAP Interpretability

Using SHAP:
- View top 10 important features for both severity and classification models
- Force plots to explain single predictions

> "SHAP analysis reveals that for every year older a vehicle is, the predicted claim amount increases by X Rand."

## ✅ Minimum Deliverables

- [x] Task 4 branch created and committed
- [x] Data cleaning & prep complete
- [x] Model pipeline ready
- [x] Evaluation metrics logged
- [x] SHAP interpretability implemented
- [x] Claim classification model trained
- [x] Risk-adjusted premium computed
- [x] README created

## 🚀 Final Results
- A classification model (e.g. XGBoostClassifier) accurately predicts claim probabilities.
- These probabilities are multiplied by predicted claim severity to produce **risk-based premium** values.
- SHAP summaries and plots offer feature-level explanations for both models, enabling transparency in pricing decisions.

## 📌 Example Risk-Based Premium Calculation
For a policyholder:
- Predicted Claim Probability = 0.27
- Predicted Claim Severity = 6,500 ZAR
- Expenses + Margin = 500 ZAR
- **Premium = (0.27 × 6500) + 500 = 2,255 ZAR**

This premium aligns with individualized risk, improving fairness and profitability.

## 📉 Predicted vs Actuals Visualization
- Scatter and KDE plots show how closely model predictions match observed claims and premiums.
- These help verify model calibration and variance.

## 🖥️ CLI for Model Serving
- A `cli_predict.py` tool enables:
  - Batch scoring of new policy data
  - JSON input/output
  - Option to serve via REST in future versions

## 📦 Exported Artifacts
- Trained model `.pkl` files saved to `/models`
- SHAP value arrays and charts saved to `/outputs/task-4/`
- CLI usage examples included in `scripts/task-4/`

## 🧭 Next Steps
- Deploy models in staging API for business integration
- Combine insights into final report with Task 1–3 findings
- Prepare stakeholder deck with visuals and KPIs
