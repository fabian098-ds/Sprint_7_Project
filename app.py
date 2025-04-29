import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la app
st.header('Análisis de anuncios de coches en USA')

# Casilla para mostrar histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma de kilometraje de los coches segmentado por su condición')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para mostrar gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión de odómetro vs precio'):
    st.write('Gráfico de dispersión: odómetro vs precio, coloreado por condición')
    fig = px.scatter(car_data, x='odometer', y='price',
                     color='condition', opacity=0.6)
    st.plotly_chart(fig, use_container_width=True)
