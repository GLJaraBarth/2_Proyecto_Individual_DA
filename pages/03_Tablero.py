import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import date, datetime, timedelta
from matplotlib.ticker import MaxNLocator
import datetime as dt
from matplotlib.ticker import FuncFormatter

# Configurar el ancho de la página a 1000 píxeles
st.set_page_config(layout="wide")

# Lee el archivo CSV y crea un DataFrame
df = pd.read_csv('Coins.csv')
df.dropna(inplace=True)

# Obtener la fecha actual
fecha_actual = dt.datetime.now()

# Calcular la fecha menos 60 días
fecha = fecha_actual - timedelta(days=60)

fecha_roi = fecha_actual - timedelta(days=365)

def pricefig(df1,coin):
       
        # Crear el gráfico
        fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

        sns.lineplot(x='date', y='price', data=df1, label='Precio')

        #maxejey = (df1['price'].max())*1.1
        #minejey = (df1['price'].min())*0.9

        # Configurar etiquetas y título
        plt.xlabel('Fecha',fontsize=8)
        plt.ylabel('Valor USD',fontsize=8)
        #plt.title(coin,fontsize=10)

        # Cambiar los límites del eje y
        #plt.ylim(minejey, maxejey)  # Cambiar los límites mínimo y máximo según tus necesidades

        # Ajustar automáticamente las etiquetas del eje x con control de separación
        intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
        locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
        plt.gca().xaxis.set_major_locator(locator)

        # Reducir tamaño de fuente de las etiquetas del eje x e y
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        plt.legend(fontsize=6)

        # Mostrar el gráfico
        st.pyplot(fig)

def EMA26plt(df1,coin):
   
    # Crear el gráfico de líneas
    fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico
    sns.lineplot(x='date', y='price', data=df1, label='Precio')
    sns.lineplot(x='date', y='EMA26', data=df1, label='EMA')
    #maxejey = (df1['price'].max())*1.1
    #minejey = (df1['price'].min())*0.9

    # Configurar etiquetas y título
    plt.xlabel('Fecha', fontsize=8)
    plt.ylabel('Valor USD', fontsize=8)
    plt.title('Media Móvil Exponencial (EMA) a Corto Plazo', fontsize=10)

    # Cambiar los límites del eje y
    #plt.ylim(minejey, maxejey)  # Cambiar los límites mínimo y máximo según tus necesidades

    # Ajustar automáticamente las etiquetas del eje x con control de separación
    intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
    locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
    plt.gca().xaxis.set_major_locator(locator)

    # Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)
    # Mostrar el gráfico
    st.pyplot(fig)

def EMA200plt(df1,coin):
   
    # Crear el gráfico de líneas
    fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico
    sns.lineplot(x='date', y='price', data=df1, label='Precio')
    sns.lineplot(x='date', y='EMA200', data=df1, label='EMA')
    #maxejey = (df1['price'].max())*1.1
    #minejey = (df1['price'].min())*0.9

    # Configurar etiquetas y título
    plt.xlabel('Fecha', fontsize=8)
    plt.ylabel('Valor USD', fontsize=8)
    plt.title('Media Móvil Exponencial (EMA) a Largo Plazo', fontsize=10)
    
    # Cambiar los límites del eje y
    #plt.ylim(minejey, maxejey)  # Cambiar los límites mínimo y máximo según tus necesidades

    # Ajustar automáticamente las etiquetas del eje x con control de separación
    intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
    locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
    plt.gca().xaxis.set_major_locator(locator)

    # Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)
    # Mostrar el gráfico
    st.pyplot(fig)

def MACD(df1,coin):
   
    # Crear el gráfico de líneas
    fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

    sns.lineplot(x='date', y='MACD', data=df1, label='MACD Line')
    sns.lineplot(x='date', y='signal_line', data=df1, label='Signal Line', color='orange')
    
    # Crear un solo gráfico de barras con barras positivas y negativas
    sns.barplot(x='date', y='Histogram', data=df1, palette=['red' if val < 0 else 'green' for val in df1['Histogram']])

    #maxejey = (df1['price'].max())*1.1
    #minejey = (df1['price'].min())*0.9

    # Configurar etiquetas y título
    plt.xlabel('Fecha', fontsize=8)
    plt.ylabel('Valor USD', fontsize=8)
    plt.title('Media Móvil de Convergencia / Divergencia (MACD)', fontsize=10)
    
    # Cambiar los límites del eje y
    #plt.ylim(minejey, maxejey)  # Cambiar los límites mínimo y máximo según tus necesidades

    # Ajustar automáticamente las etiquetas del eje x con control de separación
    intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
    locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
    plt.gca().xaxis.set_major_locator(locator)

    # Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)
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
        plt.xlabel('Fecha',fontsize=8)
        plt.ylabel('Valor',fontsize=8)
        #plt.title(coin)

        # Formatear el eje y en millones
        formatter = FuncFormatter(millions)
        plt.gca().yaxis.set_major_formatter(formatter)

        # Ajustar automáticamente las etiquetas del eje x con control de separación
        intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
        locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
        plt.gca().xaxis.set_major_locator(locator)

        # Reducir tamaño de fuente de las etiquetas del eje x e y
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        plt.legend(fontsize=6)

        # Mostrar el gráfico
        st.pyplot(fig)

def volnegfig(df1,coin):

        # Crear el gráfico
        fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

        sns.lineplot(x='date', y='total_volume', data=df1, label='Volumen Negociado', color='green')

        # Configurar etiquetas y título
        plt.xlabel('Fecha',fontsize=8)
        plt.ylabel('Valor',fontsize=8)
        #plt.title(coin)

        # Formatear el eje y en millones
        formatter = FuncFormatter(millions)
        plt.gca().yaxis.set_major_formatter(formatter)

        # Ajustar automáticamente las etiquetas del eje x con control de separación
        intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
        locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
        plt.gca().xaxis.set_major_locator(locator)

        # Reducir tamaño de fuente de las etiquetas del eje x e y
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        plt.legend(fontsize=6)

        # Mostrar el gráfico
        st.pyplot(fig)

def rsi(df1,coin):
   
    # Crear el gráfico de líneas
    fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

    sns.lineplot(x='date', y='rsi', data=df1, label='RSI')
    #sns.lineplot(x='date', y='signal_line', data=df1, label='Signal Line', color='orange')
    
    # Agregar líneas rojas en los niveles 30 y 70
    plt.axhline(y=30, color='red', linestyle='--', label='Nivel 30')
    plt.axhline(y=70, color='red', linestyle='--', label='Nivel 70')

    # Configurar etiquetas y título
    plt.xlabel('Fecha', fontsize=8)
    plt.ylabel('%', fontsize=8)
    plt.title('Índice de Fuerza Relativa (RSI)', fontsize=10)
    
    # Cambiar los límites del eje y
    #plt.ylim(minejey, maxejey)  # Cambiar los límites mínimo y máximo según tus necesidades

    # Ajustar automáticamente las etiquetas del eje x con control de separación
    intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
    locator = MaxNLocator(integer=True, nbins=intervalo_etiquetas)
    plt.gca().xaxis.set_major_locator(locator)

    # Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)
    # Mostrar el gráfico
    st.pyplot(fig)   

def valorMACD(df1,coin):
    # Obtener el valor máximo de la columna timestamp
    filtro1 = df1['timestamp'].max()

    # Filtrar el DataFrame utilizando el valor máximo de timestamp
    df2 = df1[df1['timestamp'] == filtro1]

    # Obtener el valor de la columna MACD del DataFrame filtrado
    valor = df2['MACD'].values[0]

    # Agregar un cuadro con el valor utilizando st.info()
    st.info(f"MACD = {round(valor,2)}")

def valorRSI(df1,coin):
    # Obtener el valor máximo de la columna timestamp
    filtro1 = df1['timestamp'].max()

    # Filtrar el DataFrame utilizando el valor máximo de timestamp
    df2 = df1[df1['timestamp'] == filtro1]

    # Obtener el valor de la columna MACD del DataFrame filtrado
    valor = df2['rsi'].values[0]

    # Agregar un cuadro con el valor utilizando st.info()
    st.info(f"%RSI = {round(valor,2)}")

def ROI(def2,coin):
    # Obtener el valor máximo de la columna timestamp
    filtro1 = df2['date'].iloc[-1]

    # Obtener la fecha actual
    fecha_1 = datetime.strptime(filtro1, "%d-%m-%Y")

    # Calcular la fecha de un año atrás
    fecha_2 = fecha_1 - timedelta(days=365)

    # Convertir la fecha al formato deseado
    filtro2 = fecha_2.strftime("%d-%m-%Y")

    # Precios de compra y venta en USD
    precio_compra = df2[df2['date'] == filtro2]['price'].iloc[0]
    precio_venta = df2[df2['date'] == filtro1]['price'].iloc[0]

    # Calcular el ROI
    ganancia = precio_venta - precio_compra
    costo = precio_compra

    roi_anual = (ganancia / costo) * 100

    st.info(f"ROI anual: {roi_anual:.2f}%")


# Crear las columnas para organizar las checkboxes en una fila
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

if col1.button('Avalanche'):
    coin = 'Avalanche'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col2.button('BNB'):
    coin = 'Binance'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col3.button('Bitcoin'):
    coin = 'Bitcoin'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col4.button('Cardano'):
    coin = 'Cardano'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col5.button('Dogecoin'):
    coin = 'Dogecoin'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col6.button('Ethereum'):
    coin = 'Ethereum'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col7.button('EOS'):
    coin = 'EOS'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col8.button('Solana'):
    coin = 'Solana'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col9.button('Tether'):
    coin = 'Tether'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)

if col10.button('USD Coin'):
    coin = 'USD Coin'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        EMA26plt(df1,coin)
    with col12:
        MACD(df1,coin)
    with col13:
        rsi(df1,coin)
    col14, col15, col16 = st.columns(3)
    with col14:
        pricefig(df1,coin)   
    with col15:
        mercapfig(df1,coin)
    with col16:
        volnegfig(df1,coin)
    col17, col18,col19 = st.columns(3)
    with col17:
        valorMACD(df1,coin)   
    with col18:
        valorRSI(df1,coin)
    with col19:
        ROI(df2,coin)