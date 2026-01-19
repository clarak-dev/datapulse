from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/telco_customers.csv")

def load_raw_data(path: Path) -> pd.DataFrame:
    """
    Carrega dados brutos a partir de um CSV.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo nao encontrado: {path}. Coloque o CSV em data/raw/ e renomeie para telco_customers.csv"
        )

    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    df = load_raw_data(RAW_PATH)

    print("DataPulse - Leitura de dados brutos")
    print("-" * 40)
    print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")

    print("\nColunas:")
    print(list(df.columns))

    print("\nAmostra (primeiras 5 linhas):")
    print(df.head())
