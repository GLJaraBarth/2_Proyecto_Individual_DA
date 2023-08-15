![Logo](https://blog.soyhenry.com/content/images/2021/02/HEADER-BLOG-NEGRO-01.jpg)

# DATA SCIENCE - PROYECTO INDIVIDUAL Nº2
# Data Analytics


Este proyecto nos sitúa en un rol de **`Analista de Datos`** en una empresa de servicios financieros para el mercado de criptomonedas.

![Logo](https://cardaniers.com/wp-content/uploads/2021/05/binance-coin.jpg)

## Contexto

Nuestra Empresa ha decidido incursionar en el mercado de criptomonedas y poder asesorar a nuestros Clientes respecto en cuales realizar sus inversiones de acuerdo al perfil.
Debido al gran número de monedas del mercado y para una primera investigación, se trabajara sobre un conjunto de 10 criptomonedas.

Se realizo una subdivisión de este con junto en tres categorías, según la recomendación de especialistas financieros:

1 - **Monedas estables o "stablecoins"** La principal característica es el factor de tener su precio "atado" al dólar, esto significa que su valor nunca varía de u$s1 y es la ideal para quienes no son muy arriesgados. Las más populares actualmente son Tether (USDT) y USD Coin (USDC). Para Clientes con un perfil ahorrista.

2 - **Monedas principales del mercado** Estas son Bitcoin (BTC) y Ethereum (ETH), con el principal argumento siendo que ambas tienden a mantener subidas constantes a largo plazo.

3 - **Monedas alternativas o "altcoins"** Son diferentes criptos que no tienen una antigüedad tan larga como el Bitcoin y por eso son vistas como inversiones más arriesgadas -además de tender a ser mucho más volátiles que las criptomonedas mencionadas en el punto 2. 
Entre las más populares en este grupo encontramos a los proyectos que buscan plantearse como alternativa a la red de contratos inteligentes establecida por Etherium -como lo son Solana (SOL), Cardano (ADA) o Avalanche (AVAX)- y las criptomonedas lanzadas por plataformas de inversión como Binance (BNB) o Crypto.com (CRO), Dogecoin(DOGE) y Shiba Inu (SHIB).

[Fuente](https://www.ambito.com/finanzas/criptomonedas/ahorrar-cuales-son-las-mejores-alternativas-protegerse-la-devaluacion-n5330435)

## Dataset

Los datos son extraídos de la [API CoinGecko](https://www.coingecko.com/).

## Análisis Exploratorio de Datos EDA

Para el trabajo de **`EDA`** se realizó, en líneas generales, el siguiente flujo de trabajo:

- Consulta de la documentación API de la página CoinGecko.

- Análisis de los endpoints para la obtención de la data.

- Elección del endpoint /coins/{id}/market_chart/range

- Se crearon y eliminaron columnas. 

- Se ejecutó info() para obtener información de los data frames( Cantidad de filas y columnas, tipos de dato, etc.).

- Se realizó la consulta de nulos.

- Se realizó la consulta de datos estadísticos de cada data frame.

El detalle y código en:
[archivo](https://github.com/GLJaraBarth/2_Proyecto_Individual_DA/blob/main/PI_Data_Analitycs_EDA.ipynb)

## Deployment

Se confecciono un dashboard y se desplego en **`Streamlit`**.
Los datos están listos para ser consultados a partir del siguiente link

[Link al Deployment](https://homepy-nnfvau8kus84x4ngiihcsj.streamlit.app/)