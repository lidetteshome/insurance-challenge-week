# Task 1 - Exploratory Data Analysis (EDA)

This notebook and supporting scripts form the foundation of our end-to-end insurance risk analytics pipeline for **AlphaCare Insurance Solutions**.

## Objective

Perform a comprehensive exploratory data analysis (EDA) on the provided insurance dataset to:
- Understand the structure and quality of the data
- Investigate key risk indicators such as **TotalClaims**, **TotalPremium**, and **LossRatio**
- Derive actionable insights based on regional and demographic breakdowns

## Repository Structure

```
insurance-challenge-week/
├── notebooks/
│   └── task-1/
│       └── eda-overview.ipynb
├── data/
│   └── MachineLearningRating_v3.csv
├── scripts/
│   └── eda_utils.py
├── outputs/
│   └── plots/
│       ├── loss_ratio_by_province.png
│       ├── dist_total_claims.png
│       ├── dist_total_premium.png
│       ├── premium_vs_claims.png
│       └── boxplot_total_claims.png
```

## Tools & Libraries
- Python 3.8+
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`, `scipy`

## Initial Observations

### 🔹 Provinces with Highest Average Loss Ratio
Based on grouped analysis of `LossRatio = TotalClaims / TotalPremium`, the following provinces show the **highest average loss ratios**:

- **Gauteng**
- **KwaZulu-Natal**
- **Eastern Cape**

These regions may warrant **higher premiums or tighter underwriting rules** due to their elevated risk.

### 🔹 Outliers in Claims or Premiums
Using **boxplots and z-scores**, we identified several extreme outliers in both `TotalClaims` and `TotalPremium`. These include:

- Claims exceeding **300,000 ZAR**, which significantly skew the mean
- Premiums above **100,000 ZAR**, although rare, should be flagged for manual review

These outliers could distort model training and require capping or transformation.

### 🔹 Skewed Distributions
- `TotalClaims` and `TotalPremium` are **highly right-skewed** with long tails
- A **log transformation** may help stabilize variance for modeling
- `CustomValueEstimate` also shows a non-normal distribution, further supporting the need for transformation or binning

## Next Steps
- Begin hypothesis testing on gender, province, and zip code segmentation
- Prepare DVC setup for tracking data versions (Task 2)
- Document findings in interim report

---

**Author**: Lidet Teshome - lidet.teshome.aastu@gmail.com  
**Week**: B5W3 – Insurance Risk & Predictive Analytics Challenge
