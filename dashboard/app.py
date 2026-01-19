import pandas as pd
from pathlib import Path
import streamlit as st

DATA_PATH = Path("data/processed/telco_customers_clean.csv")

st.set_page_config(page_title="DataPulse", layout="wide")

st.title("📊 DataPulse — Plataforma de Analytics")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# KPIs
total_customers = df.shape[0]
churn_rate = (df["Churn"] == "Yes").mean()
avg_ticket = df["MonthlyCharges"].mean()
avg_tenure = df["tenure"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Clientes", f"{total_customers}")
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("Ticket Médio", f"R$ {avg_ticket:.2f}")
col4.metric("Tempo Médio (meses)", f"{avg_tenure:.1f}")

st.divider()

# Churn por tempo de contrato
bins = [0, 12, 24, 48, 1000]
labels = ["0-12 meses", "13-24 meses", "25-48 meses", "48+ meses"]
df["tenure_group"] = pd.cut(df["tenure"], bins=bins, labels=labels)

churn_tenure = (
    df.groupby("tenure_group")["Churn"]
    .apply(lambda x: (x == "Yes").mean())
)

st.subheader("📉 Churn por Tempo de Contrato")
st.bar_chart(churn_tenure)

# Churn por faixa de ticket
df["charge_group"] = pd.qcut(df["MonthlyCharges"], q=3, labels=["Baixo", "Médio", "Alto"])

churn_ticket = (
    df.groupby("charge_group")["Churn"]
    .apply(lambda x: (x == "Yes").mean())
)

st.subheader("💰 Churn por Faixa de Ticket")
st.bar_chart(churn_ticket)
