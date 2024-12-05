import streamlit as st
import pandas as pd
import os
import plotly.express as px

filepath = os.path.abspath(os.path.join('.', 'data', 'sentiment_analysis.csv'))
df = pd.read_csv(filepath)

st.title("Analise de Sentimentos: Falas dos Simpsons")

fig = px.pie(df, values='counts', names='sentiment', title='Distribuicao de Sentimentos')
st.plotly_chart(fig)

