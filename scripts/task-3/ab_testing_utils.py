import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, chi2_contingency


def calculate_kpis(df):
    df = df.copy()
    df['ClaimOccurred'] = df['TotalClaims'] > 0
    df['ClaimFrequency'] = df['ClaimOccurred'].astype(int)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df


def compare_groups_ttest(df, group_col, metric_col, group_a, group_b):
    group1 = df[df[group_col] == group_a][metric_col].dropna()
    group2 = df[df[group_col] == group_b][metric_col].dropna()

    stat, p = ttest_ind(group1, group2, equal_var=False)
    return {
        "group_a": group_a,
        "group_b": group_b,
        "metric": metric_col,
        "mean_a": group1.mean(),
        "mean_b": group2.mean(),
        "p_value": p,
        "test": "Welch's T-test",
        "reject_null": p < 0.05
    }


def compare_groups_chi2(df, group_col, condition_col, group_a, group_b):
    a = df[df[group_col] == group_a][condition_col].value_counts()
    b = df[df[group_col] == group_b][condition_col].value_counts()

    # Align indices in case one group lacks a class
    contingency_table = pd.DataFrame([a, b]).fillna(0).astype(int).values
    stat, p, dof, expected = chi2_contingency(contingency_table)

    return {
        "group_a": group_a,
        "group_b": group_b,
        "condition": condition_col,
        "p_value": p,
        "test": "Chi-squared Test",
        "reject_null": p < 0.05
    }


def print_test_result(result):
    print("\n🔍 A/B Test Result")
    print("--------------------------")
    for key, value in result.items():
        print(f"{key}: {value}")
    print("--------------------------")
