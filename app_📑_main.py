#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 19:54:05 2022

@author: cspoerer
"""
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_trainnig = st.container()

with header:
    st.title("Hites: Fuga de Clientes")
    #col1, col2 = st.columns([1,1])
    st.markdown("## A través de esta aplicación podrás monitorear la fuga de clientes")
    st.markdown("### Te mostraremos paso a pase el porqué los clientes se fugan y te entregaremos una recomendación para la retencion")
    col1, col2 = st.columns([1,1])
    

with dataset:
    col3, col4 = st.columns([1,1])
    col3.header("Se observan los 5 primeros registros del Dataset LOCAL")
    df = pd.read_csv("LOCAL.csv", sep = ";")
    col4.write(df.head())
    plt.bar(df.CANAL.value_counts().index, df.CANAL.value_counts().tolist())
    plt.show()
