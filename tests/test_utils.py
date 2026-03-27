import pandas as pd
from app.utils import filter_data, calculate_metrics

def sample_df():
    return pd.DataFrame([
        {"id": 1, "status": "Aberto", "prioridade": "Alta"},
        {"id": 2, "status": "Fechado", "prioridade": "Média"},
        {"id": 3, "status": "Aberto", "prioridade": "Baixa"},
    ])

def test_filter_by_status():
    df = sample_df()
    result = filter_data(df, "Aberto", "Todos")
    assert len(result) == 2

def test_filter_by_priority():
    df = sample_df()
    result = filter_data(df, "Todos", "Média")
    assert len(result) == 1

def test_calculate_metrics():
    df = sample_df()
    total, abertos, fechados = calculate_metrics(df)
    assert total == 3
    assert abertos == 2
    assert fechados == 1