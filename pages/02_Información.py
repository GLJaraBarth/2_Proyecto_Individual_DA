import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FuncFormatter

# Configurar el ancho de la página a 1000 píxeles
st.set_page_config(layout="wide")

# Lee el archivo CSV y crea un DataFrame
df = pd.read_csv('Coins.csv')
df.dropna(inplace=True)

def pricefig(df1,coin):
       
        # Crear el gráfico
        fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

        sns.lineplot(x='date', y='price', data=df1, label='Precio')

        maxejey = (df1['price'].max())*1.1
        minejey = (df1['price'].min())*0.9

        # Configurar etiquetas y título
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.title(coin)

        # Cambiar los límites del eje y
        plt.ylim(minejey, maxejey)  # Cambiar los límites mínimo y máximo según tus necesidades

        # Ajustar automáticamente las etiquetas del eje x con control de separación
        intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
        locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
        plt.gca().xaxis.set_major_locator(locator)

        plt.legend()
        # Mostrar el gráfico
        st.pyplot(fig)

# Función para formatear los valores en millones
def millions(x, pos):
    'The two args are the value and tick position'
    return f'{x/1e6:.0f}M'

def mercapfig(df1,coin):

        # Crear el gráfico
        fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

        sns.lineplot(x='date', y='market_cap', data=df1, label='Mercado de Capitalización', color='red')

        # Configurar etiquetas y título
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.title(coin)

        # Formatear el eje y en millones
        formatter = FuncFormatter(millions)
        plt.gca().yaxis.set_major_formatter(formatter)

        # Ajustar automáticamente las etiquetas del eje x con control de separación
        intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
        locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
        plt.gca().xaxis.set_major_locator(locator)

        plt.legend()
        # Mostrar el gráfico
        st.pyplot(fig)

def volnegfig(df1,coin):

        # Crear el gráfico
        fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

        sns.lineplot(x='date', y='total_volume', data=df1, label='Volumen Negociado', color='green')

        # Configurar etiquetas y título
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.title(coin)

        # Formatear el eje y en millones
        formatter = FuncFormatter(millions)
        plt.gca().yaxis.set_major_formatter(formatter)

        # Ajustar automáticamente las etiquetas del eje x con control de separación
        intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
        locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
        plt.gca().xaxis.set_major_locator(locator)

        plt.legend()
        # Mostrar el gráfico
        st.pyplot(fig)


# Crear las columnas para organizar las checkboxes en una fila
col1, col2 = st.columns(2)

if col1.button('Avalanche'):
    coin = 'Avalanche'
    filtro = (df['nombre'] == 'Avalanche')
    df1 = df[filtro]
    pricefig(df1,coin)
    mercapfig(df1,coin)
    volnegfig(df1,coin)

if col2.button('BNB'):
    coin = 'Binance'
    filtro = (df['nombre'] == 'Binance')
    df1 = df[filtro]
    pricefig(df1,coin)
    mercapfig(df1,coin)
    volnegfig(df1,coin)
