import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Importuri
from preprocessing import *
from statistics_module import *
from visualization_module import *
from clustering_module import *
from regression_module import *
from geo_module import *

# Configurare pagina
st.set_page_config(page_title="Analiza Econometrica Avansata", layout="wide")

@st.cache_data
def load_data():
    """Incarca un esantion reprezentativ de 1000 de randuri"""
    if not os.path.exists("data.csv"):
        # Limitam la 1000 de randuri pentru eficienta maxima
        df_full = sns.load_dataset('diamonds')
        df_small = df_full.head(1000)
        df_small.to_csv("data.csv", index=False)
    return pd.read_csv("data.csv")

# Initializare date
df = load_data()

st.title("Sistem Integrat de Analiza si Predictie Economica")
st.write(f"Studiu de caz: Analiza pe un esantion optimizat de {len(df)} inregistrari")
st.markdown("---")

# Structura pe Tab-uri
tabs = st.tabs([
    "Statistici si Preprocesare",
    "Analiza Geografica",
    "Clustering Interactiv",
    "Modele de Regresie"
])

# --- TAB 1: STATISTICI SI PREPROCESARE ---
with tabs[0]:
    st.subheader("Curatarea Datelor si Analiza Descriptiva")

    # Aplicare functii din preprocessing.py
    df_clean = handle_missing_values(df)
    df_clean = remove_outliers(df_clean, 'price')

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("Statistici Descriptive:")
        st.dataframe(basic_statistics(df_clean))

        st.write("Analiza pe grupuri (Pret mediu per Taietura):")
        st.write(group_analysis(df_clean))

    with col2:
        st.write("Distributia Preturilor:")
        st.pyplot(histogram(df_clean, "price"))

        st.write("Matricea de Corelație:")
        st.pyplot(correlation_matrix(df_clean))

    st.info("Nota: Esantionul de 1000 de randuri asigura o procesare rapida si rezultate concludente.")

# --- TAB 2: ANALIZA GEOGRAFICA ---
with tabs[1]:
    st.subheader("Distributia Spatiala a Centrelor Logistice")
    st.pyplot(display_geo_analysis())

# --- TAB 3: CLUSTERING ---
with tabs[2]:
    st.subheader("Segmentarea Automata a Pietei")
    k_val = st.slider("Selectati numarul de clustere (K):", 2, 6, 3)

    X_encoded = encode_data(df_clean).select_dtypes(include=['number']).drop("price", axis=1)
    X_scaled = scale_data(X_encoded)

    clusters = run_clustering(X_scaled, k=k_val)
    df_plot = df_clean.copy()
    df_plot['Cluster'] = clusters

    fig_cluster, ax_cluster = plt.subplots()
    sns.scatterplot(data=df_plot, x='carat', y='price', hue='Cluster', palette='viridis', ax=ax_cluster)
    plt.title(f"Segmentare in {k_val} Grupuri")
    st.pyplot(fig_cluster)

# --- TAB 4: REGRESIE ---
with tabs[3]:
    st.subheader("Analiza de Regresie Multipla si Clasificare")

    # 1. Regresie Multipla (OLS)
    st.markdown("#### Model OLS (Ordinary Least Squares)")
    features = st.multiselect(
        "Variabile independente:",
        ['carat', 'depth', 'table', 'x', 'y', 'z'],
        default=['carat', 'depth']
    )

    if features:
        y_reg = df_clean["price"]
        X_reg = df_clean[features]
        model_ols = multiple_regression(X_reg, y_reg)
        st.write(model_ols.summary())

    st.markdown("---")

    # 2. Regresie Logistica
    st.markdown("#### Model de Clasificare Logistica")
    pret_mediu = df_clean['price'].median()
    y_binary = (df_clean['price'] > pret_mediu).astype(int)

    X_log = encode_data(df_clean).select_dtypes(include=['number']).drop("price", axis=1)
    X_log_scaled = scale_data(X_log)

    accuracy, report = logistic_regression(X_log_scaled, y_binary)

    st.metric("Acuratete Model", f"{accuracy:.2f}%")
    st.text("Raport de Clasificare:")
    st.text(report)
