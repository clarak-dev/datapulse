from pathlib import Path
import pandas as pd

PROCESSED_PATH = Path("data/processed/telco_customers_clean.csv")

def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    return pd.read_csv(path)

def churn_by_tenure(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analisa churn por faixa de tempo de contrato.
    """
    bins = [0, 12, 24, 48, 1000]
    labels = ["0-12 meses", "13-24 meses", "25-48 meses", "48+ meses"]

    df = df.copy()
    df["tenure_group"] = pd.cut(df["tenure"], bins=bins, labels=labels)

    result = (
        df.groupby("tenure_group")["Churn"]
        .apply(lambda x: (x == "Yes").mean())
        .reset_index(name="churn_rate")
    )

    return result

def churn_by_charges(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analisa churn por faixa de ticket mensal.
    """
    bins = df["MonthlyCharges"].quantile([0, 0.33, 0.66, 1]).values
    labels = ["Baixo", "Medio", "Alto"]

    df = df.copy()
    df["charge_group"] = pd.cut(df["MonthlyCharges"], bins=bins, labels=labels, include_lowest=True)

    result = (
        df.groupby("charge_group")["Churn"]
        .apply(lambda x: (x == "Yes").mean())
        .reset_index(name="churn_rate")
    )

    return result

if __name__ == "__main__":
    df = load_data(PROCESSED_PATH)

    print("DataPulse — Insights de Churn")
    print("-" * 40)

    tenure_insight = churn_by_tenure(df)
    print("\nChurn por tempo de contrato:")
    print(tenure_insight)

    charge_insight = churn_by_charges(df)
    print("\nChurn por faixa de ticket:")
    print(charge_insight)
