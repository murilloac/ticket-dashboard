import streamlit as st
import pandas as pd
from utils import load_data, filter_data, calculate_metrics

st.set_page_config(page_title="Ticket Dashboard", layout="wide")

st.title("📊 Ticket Dashboard")
st.markdown("Dashboard operacional de tickets com foco em organização, automação e boas práticas DevOps.")

df = load_data("app/data/tickets.csv")

st.sidebar.header("🔎 Filtros")

status_options = ["Todos"] + sorted(df["status"].unique().tolist())
priority_options = ["Todos"] + sorted(df["prioridade"].unique().tolist())

selected_status = st.sidebar.selectbox("Status", status_options)
selected_priority = st.sidebar.selectbox("Prioridade", priority_options)

filtered_df = filter_data(df, selected_status, selected_priority)

total, abertos, fechados = calculate_metrics(filtered_df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Tickets", total)

with col2:
    st.metric("Tickets Abertos", abertos)

with col3:
    st.metric("Tickets Fechados", fechados)

st.subheader("📋 Lista de Tickets")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("📈 Tickets por Status")
status_count = filtered_df["status"].value_counts()

if not status_count.empty:
    st.bar_chart(status_count)
else:
    st.warning("Nenhum ticket encontrado com os filtros selecionados.")