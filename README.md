# DataPulse

Plataforma de **analytics corporativo** desenvolvida para simular um fluxo completo de dados,
do processamento à geração de **KPIs**, **insights** e **visualização em dashboard**.

Projeto com foco em **análise de churn** e boas práticas de organização de pipelines de dados
em Python, voltado para contextos de empresas de serviços recorrentes (telecom, bancos, etc.).

---

## 🎯 Objetivo

Demonstrar, de forma prática, um pipeline de dados **ponta a ponta**, incluindo:

- Ingestão de dados
- Tratamento e padronização
- Cálculo de KPIs
- Geração de insights analíticos
- Visualização em dashboard interativo

---

## 🧱 Estrutura do Projeto

```text
datapulse/
├── src/
│   ├── load_data.py
│   ├── transform_data.py
│   ├── kpis.py
│   └── insights.py
├── painel/
│   └── app.py
├── dados/
│   ├── raw/
│   └── processed/
├── README.md
├── requirements.txt
└── .gitignore
📊 KPIs Analisados
Total de clientes

Churn rate (%)

Ticket médio mensal

Tempo médio de contrato

Churn por tempo de contrato

Churn por faixa de valor mensal

💡 Principais Insights
Clientes com menor tempo de contrato apresentam maior taxa de churn

Contratos mais longos tendem a maior retenção

Faixas de ticket médio apresentam comportamentos distintos de evasão

🛠️ Tecnologias
Python

Pandas

SQLite

Streamlit

Git / GitHub

▶️ Execução do Projeto
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar pipeline
python src/load_data.py
python src/transform_data.py
python src/kpis.py
python src/insights.py

# Executar dashboard
streamlit run painel/app.py
📌 Observações
Os dados utilizados não são versionados, seguindo boas práticas de engenharia de dados

O repositório contém apenas código, estrutura e documentação

Projeto desenvolvido com foco em simulação de cenários reais de negócio


