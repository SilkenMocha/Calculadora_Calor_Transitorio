import math
import streamlit as st
import pandas as pd
import numpy as np


def parametros_concentrados():

    with st.form(key='calc_parametros_concentrados'):
        #Valores de temperatura#
        st.subheader('Valores de temperatura')
        T0 = st.number_input('Valor de T0: ', value= 5)
        Tinf = st.number_input('Valor de T∞: ', value = 95)
        T_t = st.number_input('Valor de T(t): ', value= 70)

        #Tf = st.number_input('Valor de Tf: ', value= 70)

        #Constantes#
        st.subheader('Constantes')
        k = st.number_input('Valor de k: ', value= 0.627)
        w = st.number_input('Valor de w: ', value= 1200)
        alpha = st.number_input('Valor de α: ', format="%.9f", step = 1e-8, value= 0.151E-6)
        
        #Propiedades físicas#
        st.subheader('Propiedades físicas')
        Cp = st.number_input('Valor de Cp: (J/kg K)', value= 4180)
        d = st.number_input('Valor de densidad: (kg/m^3)', value= 3)
        
        
        #tol = st.number_input('Tolerancia: ', format="%.4f", step = 1e-4, value = 0.001 )
        #n0 = st.number_input('Iteraciones: ', value = 100)
        calcular = st.form_submit_button('Calcular')