import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import FuncFormatter
import locale

# Configurar el ancho de la página a 1000 píxeles
st.set_page_config(layout="wide")

# Lee el archivo CSV y crea un DataFrame
df = pd.read_csv('Coins.csv')
df.dropna(inplace=True)

def pricefig(df1, coin):
    # Crear el gráfico
    fig = plt.figure(figsize=(6, 3))  # Opcional: ajustar el tamaño del gráfico

    # Seleccionar los últimos 180 días de datos
    last_180_days = df1.tail(180)

    sns.lineplot(x='date', y='price', data=last_180_days, label='Precio', linewidth=0.5)  # Ajustar el grosor de la línea

    # Ajustar automáticamente las etiquetas del eje x con control de separación
    intervalo_etiquetas = 5  # Mostrar solo 10 etiquetas en el eje x
    locator = plt.MaxNLocator(integer=True, nbins=intervalo_etiquetas)
    plt.gca().xaxis.set_major_locator(locator)

    # Configurar etiquetas y título
    plt.xlabel('Fecha', fontsize=8)
    plt.ylabel('USD', fontsize=8)
    plt.title('')

    # Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


def roi30(df1, coin):
    # Crear el gráfico
    fig = plt.figure(figsize=(4, 2))  # Opcional: ajustar el tamaño del gráfico       

    # Filtrar los últimos 30 días del DataFrame
    df_last_30_days = df1.tail(30)

    # Crear un histplot en lugar de un distplot con barras claras y sin contorno
    ax = sns.histplot(data=df_last_30_days, x='ROI30', bins=10, kde=True, color='#A9CCE3', edgecolor='none')

    # Cambiar el color de la línea KDE a negro
    ax.lines[0].set_color('blue')

    plt.xlabel('')
    plt.ylabel('')
    plt.title('ROI 30 días', fontsize=6)

    #Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

def roi90(df1, coin):
    # Crear el gráfico
    fig = plt.figure(figsize=(4, 2))  # Opcional: ajustar el tamaño del gráfico       

    # Filtrar los últimos 30 días del DataFrame
    df_last_90_days = df1.tail(90)

    # Crear un histplot en lugar de un distplot con barras claras y sin contorno
    ax = sns.histplot(data=df_last_90_days, x='ROI90', bins=10, kde=True, color='#A9CCE3', edgecolor='none')

    # Cambiar el color de la línea KDE a negro
    ax.lines[0].set_color('blue')

    plt.xlabel('')
    plt.ylabel('')
    plt.title('ROI 90 días', fontsize=6)

    #Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

def roi180(df1, coin):
    # Crear el gráfico
    fig = plt.figure(figsize=(4, 2))  # Opcional: ajustar el tamaño del gráfico       

    # Filtrar los últimos 30 días del DataFrame
    df_last_180_days = df1.tail(180)

    # Crear un histplot en lugar de un distplot con barras claras y sin contorno
    ax = sns.histplot(data=df_last_180_days, x='ROI180', bins=10, kde=True, color='#A9CCE3', edgecolor='none')

    # Cambiar el color de la línea KDE a negro
    ax.lines[0].set_color('blue')

    plt.xlabel('')
    plt.ylabel('')
    plt.title('ROI 180 días', fontsize=6)

    #Reducir tamaño de fuente de las etiquetas del eje x e y
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    plt.legend(fontsize=6)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)




st.markdown('<p style="font-size:36px; font-weight:bold; text-align:left;">Análisis a Plazos de Inversión</p>', unsafe_allow_html=True)

# Crear las columnas para organizar las checkboxes en una fila
col1, col2 = st.columns(2)

coin = 'USD Coin'
filtro = (df['nombre'] == coin)
df1 = df[filtro]
with col1:
        pricefig(df1,coin)
with col2:
        st.markdown('<p style="font-size:36px; font-weight:bold; text-align:center; color:green;">USD Coin (USDC)</p>', unsafe_allow_html=True)
        st.markdown('')
        show_value = st.markdown(
        f"<div style='text-align:right; font-size:32px; padding-right:30px;'>"
        f"CAPITALIZACION DE MERCADO"
        f"</div>",
        unsafe_allow_html=True
        )

        if show_value:
                # Mostrar el valor en un recuadro con letras más grandes y ubicado hacia la derecha
                last_market_cap = df1['market_cap'].iloc[-1]
                last_market_cap_millions = last_market_cap / 1e6  # Convertir a millones

                # Configurar la localización para usar el punto como separador de miles
                locale.setlocale(locale.LC_ALL, '')  # Usar la configuración regional actual

                # Formatear el valor con separador de miles
                formatted_value = locale.format_string("%.0f", last_market_cap_millions, grouping=True)

                st.markdown(
                        f"<div style='text-align:right; font-size:32px; padding-right:30px;'>"
                        f"{formatted_value} M USD"
                        f"</div>",
                        unsafe_allow_html=True
                )


        st.markdown('')

        show_value = st.markdown(
        f"<div style='text-align:right; font-size:32px; padding-right:30px;'>"
        f"VOLUMEN NEGOCIADO"
        f"</div>",
        unsafe_allow_html=True
        )

        if show_value:
                # Mostrar el valor en un recuadro con letras más grandes y ubicado hacia la derecha
                last_total_volume = df1['total_volume'].iloc[-1]
                last_total_volume_millions = last_total_volume / 1e6  # Convertir a millones

                # Configurar la localización para usar el punto como separador de miles
                locale.setlocale(locale.LC_ALL, '')  # Usar la configuración regional actual

                # Formatear el valor con separador de miles
                formatted_value = locale.format_string("%.0f", last_total_volume_millions, grouping=True)

                st.markdown(
                        f"<div style='text-align:right; font-size:32px; padding-right:30px;'>"
                        f"{formatted_value} M USD"
                        f"</div>",
                        unsafe_allow_html=True
                )

col3, col4, col5 = st.columns(3)    
with col3:
        st.markdown('<p style="font-size: 24px;"><b>Corto Plazo</b></p>', unsafe_allow_html=True)
        roi30(df1,coin)
with col4:
        st.markdown('<p style="font-size: 24px;"><b>Mediano Plazo</b></p>', unsafe_allow_html=True)
        roi90(df1,coin)
with col5:
        st.markdown('<p style="font-size: 24px;"><b>Largo Plazo</b></p>', unsafe_allow_html=True)
        roi180(df1,coin)