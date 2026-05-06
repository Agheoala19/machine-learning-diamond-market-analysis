import pandas as pd
from sklearn.preprocessing import StandardScaler

def handle_missing_values(df):
    return df.fillna(df.mean(numeric_only=True))

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

def encode_data(df):
    return pd.get_dummies(df, drop_first=True)

def scale_data(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
