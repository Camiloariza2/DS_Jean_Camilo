import numpy as np
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Files/Airplane_Crashes_and_Fatalities_Since_1908.csv')
df_p =df
df.head(100)

df.shape

print(type(df_p))
df_p.dtypes

df['Aboard'] = df['Aboard'].fillna(0)
df['Aboard'] = df['Aboard'].astype(int)

df['Fatalities'] = df['Fatalities'].fillna(0)
df['Fatalities'] = df['Fatalities'].astype(int)

df['Ground'] = df['Ground'].fillna(0)
df['Ground'] = df['Ground'].astype(int)

df_p.keys()

#'09/17/1908'
df_p_fecha = df_p['Date']
df_p_fecha = pd.to_datetime(df_p['Date'], format = '%m/%d/%Y')
df_p_fecha

df_p['Flight #'].replace('-',0)

df['Date'] = df_p_fecha
df