# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:17:18 2023

@author: ep_blizarme
"""

import pandas as pd
import datetime as dt

#%% df0
df0  = pd.read_excel("UNIDADES DE GENERACION JULIO 2023_PRELIMINAR.xlsx", "Diccionario",skiprows=2,header = 1).fillna(0)
df0 = df0.drop(index=[0],axis=0)
df0 = df0.drop(columns= df0.columns[8:len(df0.columns)])


print(list(range(10,len(df0.columns))))

#%% df1
df1  = pd.read_excel("UNIDADES DE GENERACION AGOSTO 2023_REUNION.xlsx", "Prueba1",skiprows=1,header = 1).fillna(0)
df1 = df1.drop(index=[0],axis=0)
df1 = df1.drop(columns= df1.columns[3:len(df1.columns)])

#%% comparacion

# Crear DataFrame df1 comparando las coincidencias en las columnas EMPRESA, UBICACION y EQUIPO
df2 = df1.merge(df0, on=["EMPRESA", "UBICACIÓN", "EQUIPO"], suffixes=("_df0", "_df1"))

# Eliminar filas duplicadas y columnas repetidas
# df2 = df2.drop_duplicates(subset=["EMPRESA", "UBICACIÓN", "EQUIPO"],keep=False)

# Mostrar df2
# print(df1)






