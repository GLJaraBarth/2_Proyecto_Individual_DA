import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FuncFormatter
import pandas as pd
import csv
import numpy as np
import datetime as dt


# Configurar el ancho de la página a 1000 píxeles
st.set_page_config(layout="wide")

# Lee el archivo CSV y crea un DataFrame
df = pd.read_csv('Coins.csv')
df.dropna(inplace=True)

# Obtener la fecha actual
fecha_actual = dt.datetime.now()

# Calcular la fecha menos 60 días
fecha = fecha_actual - dt.timedelta(days=60)

fecha_roi = fecha_actual - dt.timedelta(days=365)

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
    plt.title('')

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
    plt.title('')
    
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
    plt.title('')
    
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
    plt.title('')
    
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



def roi(df, plazo):
    if plazo == 30:
        roi = 'ROI30'
    if plazo == 90:
        roi = 'ROI90'
    if plazo == 180:
        roi = 'ROI180'

    fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

    # Seleccionar los últimos registros de cada categoría
    #ultimos_registros = df.groupby('nombre').last().reset_index()

    # Ordenar el DataFrame en función de la columna "column_name" de manera ascendente
    df_sorted = df.sort_values(by="date", ascending=True)

    df_last = df_sorted.tail(10)

    # Definir una función para determinar los colores basados en los valores de 'ROI30'
    def color_palette(val):
        if val < 0:
            return 'red'
        else:
            return 'green'

    # Crear una lista de colores basada en los valores de 'ROI30'
    colors = [color_palette(val) for val in df_last[roi]]

    # Crear el gráfico de barras con colores personalizados
    ax = sns.barplot(data=df_last, x='nombre', y=roi, palette=colors)

    plt.title(f'')  # Título con el valor del plazo
    plt.xlabel('')
    plt.ylabel('ROI')

    # Rotar las etiquetas del eje x a 45 grados
    plt.xticks(rotation=45)

    # Ajustar automáticamente las etiquetas del eje y con control de separación
    intervalo_etiquetas_y = 5  # Mostrar solo 5 etiquetas en el eje y
    locator_y = plt.MaxNLocator(integer=True, nbins=intervalo_etiquetas_y)
    plt.gca().yaxis.set_major_locator(locator_y)

    # Ajustar tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


# Crear las columnas para organizar las checkboxes en una fila
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

if col1.button('Avalanche'):
    coin = 'Avalanche'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)

if col2.button('BNB'):
    coin = 'BNB'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col3.button('Bitcoin'):
    coin = 'Bitcoin'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col4.button('Cardano'):
    coin = 'Cardano'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col5.button('Dogecoin'):
    coin = 'Dogecoin'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col6.button('Ethereum'):
    coin = 'Ethereum'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col7.button('EOS'):
    coin = 'EOS'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col8.button('Solana'):
    coin = 'Solana'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col9.button('Tether'):
    coin = 'Tether'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)


if col10.button('USD Coin'):
    coin = 'USD Coin'
    # Filtrar el DataFrame con la condición AND
    #fecha_actual = datetime.date.today()
    fecha_inicio = fecha_actual - dt.timedelta(days=180)
    fecha_EMA26 = pd.to_datetime(fecha_inicio)
    # Convertir cada valor en la columna 'date' a un objeto Timestamp
    df['timestamp'] = pd.to_datetime(df['date'])
    filtro = (df['timestamp'] >= fecha_EMA26) & (df['nombre'] == coin)
    filtro2 = df['nombre'] == coin
    df1 = df[filtro]
    df2 = df[filtro2]
    col11, col12,col13 = st.columns(3)
    with col11:
        st.text('Media Móvil Exponencial (EMA) a Corto Plazo')
        EMA26plt(df1,coin)
    with col12:
        st.text('Media Móvil de Convergencia / Divergencia (MACD)')
        MACD(df1,coin)
    with col13:
        st.text('Índice de Fuerza Relativa (RSI)')
        rsi(df1,coin)
    col14, col15 = st.columns(2)
    with col14:
        valorMACD(df1,coin)
    with col15:
        valorRSI(df1,coin)
    col16, col17,col18 = st.columns(3)
    with col16:
        st.text('ROI a Corto Plazo')
        roi(df, 30)  
    with col17:
        st.text('ROI a Mediano Plazo')
        roi(df, 90)
    with col18:
        st.text('ROI a Largo Plazo')
        roi(df, 180)
