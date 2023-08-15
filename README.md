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


- 

- 

- 

El detalle y código en:
[archivo](https://github.com/GLJaraBarth/1_Proyecto_Individual_MLOps/blob/main/steam_games_EDA_DE.ipynb)


## Desarrollo API

Se disponibilizaron los siguientes endpoints a través del Framework **`FastAPI`**:

- def genero( Año: str ): Se ingresa un año y devuelve una lista con los 5 géneros más vendidos en el orden correspondiente. 
  
  p.e. genero '2010' en string y retorna {'Anio': 2010,'Generos': ['Action', 'Indie', 'Strategy', 'Adventure', 'Casual']}

- def juegos( Año: str ): Se ingresa un año y devuelve una lista con los juegos lanzados en el año. 
 
  p.e. juegos '2019' en sring y retorna {'Anio': 2019,'Juegos': ['Raji: An Ancient Epic',"K'NOSSOS",'The Legendary Player - Make Your Reputation - OPEN BETA','The End of an Age: Fading Remnants']}

- def specs( Año: str ): Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente. 
  
  p.e. specs '2018' en string y retorna {'Anio': 2018,'Specs': ['Single-player','Steam Achievements','Full controller support','Steam Cloud','Partial Controller Support']}

- def earlyacces( Año: str ): Cantidad de juegos lanzados en un año con early access. 
  
  p.e. earlyacces '2013' en string y retorna {'Anio': 2013, 'Cantidad de Juegos con early access': 10}

- def sentiment( Año: str ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con   un análisis de sentimiento.

                    Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}

    p.e. sentiment '2018' en string y retorna {'Anio': 2018,'Cantidad de registros categorizados': {'Sin Datos': 146,'Mixed': 6,'Mostly Positive': 3,'Very Positive': 3,'Mostly Negative': 1}}

- def metascore( Año: str ): Top 5 juegos según año con mayor metascore. 
  
  p.e.metascore '2015' en string y retorna {'Anio': 2015,'Top 5 de juegos   con mayor metascore': ['Grand Theft Auto V','Divinity: Original Sin - Enhanced Edition','Undertale','METAL GEAR SOLID V: THE PHANTOM PAIN','Pillars of Eternity']}

El código para correr la API dentro de FastAPI se puede visualizar [aquí](https://github.com/GLJaraBarth/1_Proyecto_Individual_MLOps/blob/main/main.py) 

## Data Engineering para Machine Learning

El análisis exploratorio de datos **`EDA`** para el modelo de **`Machine Learning`** se realizó, en líneas generales, en el siguiente flujo de trabajo:

- Lectura del archivo PARQUET y creación del Data Frame.

- Identificación de features importantes (Eliminación de irrelevantes y/o redundantes).

- Transformaciones (Cambio de tipo de datos, One-Hot Encoding, Label Encoder)

- Estadísticas descriptivas (Detección de outliers).

- Tratamiento de Outliers (Para asumir valores atípicos, se usa la Regla de las Tres Sigmas).

- Análisis de variables (Mediante Histogramas, Boxplots y Scatterplots).

- Matrices de correlación.

- Exportación.

El detalle y código en:
[archivo](https://github.com/GLJaraBarth/1_Proyecto_Individual_MLOps/blob/main/steam_games_EDA_ML.ipynb)

## Modelo de predicción - Machine Learning

Para el modelo de predicción en **`Machine Learning`** se utilizó como criterio filtrar el dataset algunos de los géneros (6 en total) y el atributo earlyacces (Se asumió que el modelo debe predecir el precio de un nuevo juego, del cual no se cuenta con información de sentiment, metascore, etc.).
Se trata de un modelo de Aprendizaje Supervisado el cual se trabajó con la librería **`Scikit-Learn`** con un algoritmo de regresión lineal múltiple.
El set de datos se dividió en 80% para entrenamiento y 20% para testeo. Para la evaluación del modelo se utilizó en RSME.

- def predicción( genero, earlyaccess = True/False): Ingresando estos parámetros, deberíamos recibir el precio y RMSE. p.e. genero 'Action', earlyaccess = True retorna {'Precio': 10.95969009399414, 'RSME': 7.25}

El detalle y código en:
[archivo](https://github.com/GLJaraBarth/1_Proyecto_Individual_MLOps/blob/main/modelo_ML.ipynb)

## Deployment

Para el deploy de la API, se utilizó la plataforma **`Render`**.
Los datos están listos para ser consumidos y consultados a partir del siguiente link

[Link al Deployment](https://gljara-1-proyecto-mlops.onrender.com/docs#)