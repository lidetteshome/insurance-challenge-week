# Task 3 - A/B Hypothesis Testing for Insurance Risk Analysis

## Objective

This task aims to statistically validate or reject key hypotheses related to insurance claim risk. The results will inform segmentation strategies for more accurate premium pricing.

## Metrics Defined

- **Claim Frequency**: % of policies with at least one claim
- **Claim Severity**: Average TotalClaims among policies with claims
- **Margin**: TotalPremium - TotalClaims

## Hypotheses Tested

| Hypothesis | Null Hypothesis (H₀) | Test Type |
|------------|----------------------|-----------|
| H1 | No risk difference across provinces | T-test / ANOVA |
| H2 | No risk difference between zip codes | ANOVA |
| H3 | No margin difference between zip codes | T-test |
| H4 | No risk difference between Women and Men | Chi-squared (Claim Frequency), T-test (Severity) |

## Files and Structure

```
notebooks/
└── task-3/
    └── hypothesis_testing.ipynb

scripts/
└── task-3/
    └── ab_testing_utils.py
```

## How to Use

1. **Prepare KPIs** using `calculate_kpis(df)`
2. **Run comparisons** with:
   - `compare_groups_ttest(...)` for numerical metrics
   - `compare_groups_chi2(...)` for binary/categorical
3. **Review outputs** with `print_test_result(...)`

## Example Interpretation

> We reject the null hypothesis (p < 0.01). Gauteng shows a 15% higher claim frequency than Western Cape. This supports regional premium adjustment.

## Insights and Action

Each result includes:
- Groups compared
- Metric means
- p-value and test type
- Clear recommendation based on significance level (α = 0.05)

## Summary and Business Implications

### Hypothesis Rejections:
- ✅ H1: Rejected. Gauteng shows a statistically significant higher claim frequency than Western Cape (p < 0.01).
- ✅ H4: Rejected. Female drivers have a slightly higher claim frequency and severity than male drivers (p < 0.05).
- ❌ H2: Not rejected. Risk differences across zip codes are not statistically significant.
- ❌ H3: Not rejected. Margin differences across zip codes do not present meaningful variation.

### Pricing Strategy Implications:
- Adjust premiums upward for **high-risk provinces like Gauteng**.
- Monitor **gender-based claim patterns**, but apply cautiously to avoid regulatory and ethical issues.
- Avoid over-segmenting on zip code until more evidence of geographic significance emerges.

### Recommendations:
- Introduce regional modifiers into pricing models (province-level).
- Investigate driver behavior or vehicle type correlation with gender to support pricing decisions.
- Maintain current zip code segmentation, but enrich with additional variables for Task 4 modeling.

---

**Author**: Lidet Teshome - lidet.teshome.aastu@gmail.com  
**Week**: B5W3 – Insurance Risk & Predictive Analytics Challenge
