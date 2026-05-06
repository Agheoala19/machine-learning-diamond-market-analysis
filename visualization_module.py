import matplotlib.pyplot as plt
import seaborn as sns

def histogram(df, column):
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    return fig

def correlation_matrix(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    return fig
