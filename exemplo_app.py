# -*_ coding utf-8 -*-

import pandas as pd

df = pd.read_csv('covid-variants.csv')

import streamlit as st

paises = list(df['location'].unique())
variantes = list(df['variant'].unique())

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

pais = st.sidebar.selectbox('Escolha o pais',['Todos'] + paises)
variante = st.sidebar.selectbox('Escolha a Variantes', ['Todas'] + variantes)

if (pais != 'Todos'):
    st.header("Mostrando resultado de " + pais)
    df = df[df['location'] == pais]

else:
    st.header("Mostrando resultado para todos os paises")

if (variante != 'Todas'):
    st.subheader("Mostrando para variante " + variante)
    df = df[df['variant'] == variante]

else:
    st.subheader("Mostrando resultado para todas as variantes")

dfShow = df.groupby(by=['date']).sum()

import plotly.express as px

fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title='Casos diários Covid-19' )
#mostra figura criada pelo plotly
st.plotly_chart(fig, use_container_width=True)
