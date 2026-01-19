from pathlib import Path
import pandas as pd

PROCESSED_PATH = Path("data/processed/telco_customers_clean.csv")

def load_processed(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    return pd.read_csv(path)

def calculate_kpis(df: pd.DataFrame) -> dict:
    """
    Calcula KPIs principais para telecom.
    """
    kpis = {}

    # Total de clientes
    kpis["total_customers"] = df.shape[0]

    # Churn rate
    if "Churn" in df.columns:
        churn_rate = (df["Churn"] == "Yes").mean()
        kpis["churn_rate"] = churn_rate

    # Ticket medio
    if "MonthlyCharges" in df.columns:
        kpis["avg_monthly_charges"] = df["MonthlyCharges"].mean()

    # Tempo medio de contrato
    if "tenure" in df.columns:
        kpis["avg_tenure_months"] = df["tenure"].mean()

    return kpis

if __name__ == "__main__":
    df = load_processed(PROCESSED_PATH)
    kpis = calculate_kpis(df)

    print("DataPulse — KPIs principais")
    print("-" * 40)

    print(f"Total de clientes: {kpis['total_customers']}")

    if "churn_rate" in kpis:
        print(f"Churn rate: {kpis['churn_rate']:.2%}")

    if "avg_monthly_charges" in kpis:
        print(f"Ticket medio mensal: R$ {kpis['avg_monthly_charges']:.2f}")

    if "avg_tenure_months" in kpis:
        print(f"Tempo medio de contrato: {kpis['avg_tenure_months']:.1f} meses")
