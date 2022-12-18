#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:16:45 2022

@author: cspoerer
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("df_cierres.csv")

df['Var 2d']=round(df['Var 2d']*100,1)
df['Var 3d']=round(df['Var 3d']*100,1)
df['Var 1d']=round(df['Var 1d']*100,1)


st.title("Cierre de Acciones")

st.write("**Top 5 más bajas ayer**")

df1 = df.sort_values(by=['Var 1d'], ascending=True)
fig, ax = plt.subplots()
sns.heatmap([df1["Var 1d"].head(5)], ax=ax, annot=True, fmt="g", cbar =False, square=True, 
            xticklabels=df1.accion.head(5), yticklabels=False, cmap="rocket")
st.write(fig)
st.write(df1.head(5))


st.write("**Top 5 más bajas hace 2 días**")

df2 = df.sort_values(by=['Var 2d'], ascending=True)
fig, ax = plt.subplots()
sns.heatmap([df1["Var 2d"].head(5)], ax=ax, annot=True,fmt="g", cbar =False, square=True, 
            xticklabels=df2.accion.head(5), yticklabels=False, cmap="rocket")
st.write(fig)
st.write(df2.head(5))

st.write("**Top 5 más bajas hace 3 días**")

df3 = df.sort_values(by=['Var 3d'], ascending=True)
fig, ax = plt.subplots()
sns.heatmap([df1["Var 3d"].head(5)], ax=ax, annot=True, fmt="g", cbar =False, square=True, 
            xticklabels=df3.accion.head(5), yticklabels=False, cmap="rocket")
st.write(fig)
st.write(df3.head(5))

st.balloons()



