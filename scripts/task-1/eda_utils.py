import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="pastel")


def load_data(filepath):
    """Loads CSV data into a DataFrame."""
    return pd.read_csv(filepath)


def summarize_data(df):
    """Returns basic summary of the DataFrame."""
    return df.describe(include='all'), df.info(), df.isnull().sum()


def plot_loss_ratio_by_group(df, group_col, output_path):
    """Plots average loss ratio by a given categorical column."""
    df = df.copy()
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    grouped = df.groupby(group_col)[
        'LossRatio'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=grouped.index, y=grouped.values)
    plt.title(f'Average Loss Ratio by {group_col}')
    plt.ylabel('Loss Ratio')
    plt.xlabel(group_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_distribution(df, col, output_path):
    """Plots distribution of a numerical column."""
    plt.figure(figsize=(10, 5))
    sns.histplot(df[col].dropna(), kde=True, bins=30)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_scatter(df, x_col, y_col, output_path):
    """Plots a scatterplot between two numerical columns."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(f'{y_col} vs {x_col}')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_boxplot(df, col, output_path):
    """Generates a boxplot for detecting outliers in a numerical column."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[col].dropna())
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
