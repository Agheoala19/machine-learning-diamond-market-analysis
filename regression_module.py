from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import statsmodels.api as sm


def multiple_regression(X, y):
    # Definirea problemei: Analiza impactului caracteristicilor asupra pretului.
    # Metode: Ordinary Least Squares (OLS).
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model


def logistic_regression(X, y_binary):
    # Definirea problemei: Clasificarea produselor in categorii de pret (High/Low).
    # Metode: Regresie Logistica cu evaluare prin raport de clasificare.
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y_binary)
    y_pred = model.predict(X)

    acc = accuracy_score(y_binary, y_pred) * 100
    report = classification_report(y_binary, y_pred)

    return acc, report
