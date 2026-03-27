import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ticket Dashboard", layout="wide")

st.title("📊 Ticket Dashboard - DevOps Portfolio Project")

@st.cache_data
def load_data():
    return pd.read_csv("app/data/tickets.csv", encoding="cp1252")

df = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Tickets", len(df))

with col2:
    abertos = len(df[df["status"] == "Aberto"])
    st.metric("Tickets Abertos", abertos)

with col3:
    fechados = len(df[df["status"] == "Fechado"])
    st.metric("Tickets Fechados", fechados)

st.subheader("Lista de Tickets")
st.dataframe(df, use_container_width=True)

st.subheader("Tickets por Status")
st.bar_chart(df["status"].value_counts())