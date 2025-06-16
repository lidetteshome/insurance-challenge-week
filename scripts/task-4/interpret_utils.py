import shap
import matplotlib.pyplot as plt

# Ensure this call once before plotting
shap.initjs()


def explain_with_shap(pipeline, X_sample):
    model = pipeline.named_steps['regressor']
    preprocessor = pipeline.named_steps['preprocessor']

    X_transformed = preprocessor.transform(X_sample)
    explainer = shap.Explainer(model.predict, X_transformed)
    shap_values = explainer(X_transformed)

    return explainer, shap_values


def plot_summary(shap_values, features, plot_type="bar"):
    shap.summary_plot(shap_values, features, plot_type=plot_type)


def plot_force(explainer, shap_values, index=0):
    return shap.plots.force(shap_values[index])
