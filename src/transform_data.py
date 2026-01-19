from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/telco_customers.csv")
PROCESSED_PATH = Path("data/processed/telco_customers_clean.csv")

def load_raw(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    return pd.read_csv(path)

def clean_telco(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpeza minima e padronizacao para analise.
    """
    df = df.copy()

    # 1) Padroniza nome de colunas (mantem como veio, mas remove espaços extras)
    df.columns = [c.strip() for c in df.columns]

    # 2) Alguns datasets vêm com TotalCharges como texto e com espaços
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # 3) MonthlyCharges deve ser numérico (normalmente já é)
    if "MonthlyCharges" in df.columns:
        df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")

    # 4) Remover linhas sem customerID (se existir)
    if "customerID" in df.columns:
        df = df.dropna(subset=["customerID"])

    # 5) Normalizar alvo churn (se existir)
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].astype(str).str.strip()

    return df

def save_processed(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df_raw = load_raw(RAW_PATH)
    df_clean = clean_telco(df_raw)
    save_processed(df_clean, PROCESSED_PATH)

    print("DataPulse - Transformacao concluida")
    print("-" * 40)
    print(f"Arquivo salvo em: {PROCESSED_PATH}")
    print(f"Linhas: {df_clean.shape[0]} | Colunas: {df_clean.shape[1]}")
    print("\nTipos (amostra):")
    print(df_clean.dtypes.head(10))
