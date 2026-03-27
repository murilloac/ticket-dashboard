import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, encoding="cp1252")

def filter_data(df: pd.DataFrame, status: str, prioridade: str) -> pd.DataFrame:
    filtered = df.copy()

    if status != "Todos":
        filtered = filtered[filtered["status"] == status]

    if prioridade != "Todos":
        filtered = filtered[filtered["prioridade"] == prioridade]

    return filtered

def calculate_metrics(df: pd.DataFrame):
    total = len(df)
    abertos = len(df[df["status"] == "Aberto"])
    fechados = len(df[df["status"] == "Fechado"])
    return total, abertos, fechados