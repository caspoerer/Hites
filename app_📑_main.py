#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 19:54:05 2022

@author: cspoerer
"""
import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_trainnig = st.beta_container()

with header:
    st.title("Hites: Fuga de Clientes")
    col1, col2 = st.columns([1,1])
    col1.markdown("# A través de esta aplicación podrás monitorear la fuga de clientes")
    col2.markdown("# Te mostraremos paso a pase el porqué los clientes se fugan y te entregaremos una recomendación para la retencion")
    

with dataset:
    col3, col4 = st.columns([1,1])
    col3.markdown("Dataset")
    df = pd.read_csv("LOCAL.csv", sep = ";")
    st.write(df.head())
