# Insurance Challenge Week – End-to-End Risk Analytics

This repository showcases an end-to-end pipeline for insurance risk modeling, including:
- Data Exploration & Cleaning
- Data Version Control
- Statistical Hypothesis Testing
- Predictive Modeling (Task 4 in progress...)

---

## Project Structure

```
insurance-challenge-week/
├── LICENSE
├── README.md
├── data
│   ├── MachineLearningRating_v3.csv
│   └── MachineLearningRating_v3.csv.dvc
├── models
│   ├── preprocessor.pkl
│   ├── probability_model.pkl
│   └── severity_model.pkl
├── notebooks
│   ├── task-1
│   │   ├── README.md
│   │   └── eda-overview.ipynb
│   ├── task-2
│   │   ├── README.md
│   │   └── task-2.sh
│   ├── task-3
│   │   ├── README.md
│   │   └── hypothesis_testing.ipynb
│   └── task-4
│       ├── README.md
│       └── modeling_pipeline.ipynb
├── outputs
│   ├── task-1
│   │   └── plots
│   │       ├── boxplot_total_claims.png
│   │       ├── dist_total_claims.png
│   │       ├── dist_total_premium.png
│   │       ├── loss_ratio_by_province.png
│   │       └── premium_vs_claims.png
│   ├── task-2
│   ├── task-3
│   └── task-4
├── requirements.txt
└── scripts
    ├── task-1
    │   ├── __pycache__
    │   │   └── eda_utils.cpython-312.pyc
    │   └── eda_utils.py
    ├── task-2
    ├── task-3
    │   ├── __pycache__
    │   │   └── ab_testing_utils.cpython-312.pyc
    │   └── ab_testing_utils.py
    └── task-4
        ├── __pycache__
        │   └── modeling_utils.cpython-312.pyc
        ├── cli_predict.py
        ├── interpret_utils.py
        ├── modeling_utils.py
        ├── test_batch.csv
        └── train_models.py
```

---

## ✅ Completed Tasks

### [Task 1 – Exploratory Data Analysis](notebooks/task-1/README.md)
- Visualized claims, premiums, and loss ratios
- Identified skewness and outliers
- Found high-loss provinces that may require premium adjustment

### [Task 2 – Data Version Control (DVC)](notebooks/task-2/README.md)
- Tracked datasets using DVC
- Set up local remote for data storage
- Integrated automation via shell script + GitHub Action

### [Task 3 – Hypothesis Testing](notebooks/task-3/README.md)
- Tested risk differences across provinces, zip codes, and genders
- Used chi-squared and t-tests with p-value interpretation
- Provided actionable pricing recommendations

### [Task 4 – Predictive Modeling (WIP)](notebooks/task-4/README.md)
- Building regression & classification models
- Risk-based premium calculation using probability × severity
- SHAP interpretability and CLI support in progress

---

## Tools & Libraries

- Python (pandas, sklearn, shap, matplotlib, seaborn)
- DVC for data versioning
- GitHub Actions for automation
- Jupyter for notebooks
- SHAP for model interpretability


---

**Author**: Lidet Teshome - lidet.teshome.aastu@gmail.com  
**Week**: B5W3 – Insurance Risk & Predictive Analytics Challenge
