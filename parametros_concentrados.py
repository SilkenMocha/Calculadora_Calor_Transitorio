import math
import streamlit as st
import pandas as pd
import numpy as np
import math


def parametros_concentrados():

    geometria = st.radio(
        "Geometria del problema",
        ('Pared', 'Cilindro', 'Esfera'))


    with st.form(key='calc_parametros_concentrados'):
        #Valores de temperatura#
        st.subheader('Valores de temperatura')
        T0 = st.number_input('Valor de T0: ', value= 5)
        Tinf = st.number_input('Valor de T∞: ', value = 95)
        T_t = st.number_input('Valor de T(t): ', value= 70)

        #Tf = st.number_input('Valor de Tf: ', value= 70)

        #Constantes#
        st.subheader('Constantes')
        k = st.number_input('Valor de k: ', format="%.4f", step = 1e-4, value= 0.627)
        h = st.number_input('Valor de h: ', value= 1200)
        alpha = st.number_input('Valor de α: ', format="%.9f", step = 1e-8, value= 0.151E-6)
        
        #Propiedades físicas#
        st.subheader('Propiedades físicas')
        Cp = st.number_input('Valor de Cp: (J/kg K)', value= 4180)
        d = st.number_input('Valor de densidad: (kg/m^3)', value= 994)
        
        if geometria == 'Pared':
            L = st.number_input('Longuitud de pared: ', format="%.4f", step = 1e-3, value= 0.025)
            V_pared = st.number_input('Volumen de pared: ', format="%.4f", step = 1e-3, value= 0.025)
            #m = st.number_input('Masa de pared: (Si hay)', format="%.4f", step = 1e-3, value= 0.025)
        
        if geometria == 'Cilindro':
            r = st.number_input('Radio del cilindro: ', format="%.4f", step = 1e-3, value= 0.025)
            ht = st.number_input('Altura del cilindro: ', format="%.4f", step = 1e-3, value= 0.5)
            #m = st.number_input('Masa de pared: (Si hay)', format="%.4f", step = 1e-3, value= 0.025)    
        if geometria == 'Esfera':
            r = st.number_input('Radio de la esfera: ', format="%.4f", step = 1e-3, value= 0.025)
            #m = st.number_input('Masa de pared: (Si hay)', format="%.4f", step = 1e-3, value= 0.025)            

        #tol = st.number_input('Tolerancia: ', format="%.4f", step = 1e-4, value = 0.001 )
        #n0 = st.number_input('Iteraciones: ', value = 100)
        calcular = st.form_submit_button('Calcular')
    
    
    if geometria == 'Pared':
    #tiempo#    
        Lc = L
        b = h/(d*Cp*Lc)
        t = (-1/b)* math.log((T_t-Tinf)/(T0-Tinf))
        st.subheader("tiempo: " + str(t))

    #Energia absorbida#
        Q = d*V_pared*Cp*(T_t-T0)
        st.subheader("tiempo: " + str(Q))
        
        col1, col2= st.columns(2)
        col1.metric("Tiempo", str(round(t,4)))
        col2.metric("Energia absorbida", str(round(Q,4)))

    if geometria == 'Cilindro':
    #tiempo#
        Lc = r/2
        b = h/(d*Cp*Lc)
        t = (-1/b)* math.log((T_t-Tinf)/(T0-Tinf))
        st.subheader("tiempo: " + str(t))

    #Energia absorbida#
        V_cilindro = (math.pi*(r**2))*ht
        Q = d*V_cilindro*Cp*(T_t-T0)
        st.subheader("Energia absorbida: " + str(Q))
        
        col1, col2= st.columns(2)
        col1.metric("Tiempo", str(round(t,4)))
        col2.metric("Energia absorbida", str(round(Q,4)))            

    if geometria == 'Esfera':
    #tiempo#
        Lc = r/3            
        b = h/(d*Cp*Lc)
        t = (-1/b)* math.log((T_t-Tinf)/(T0-Tinf))
    
    #Energia absorbida#
        V_esfera = (4/3)*(math.pi*(r**3))
        Q = d*V_esfera*Cp*(T_t-T0)
        
        col1, col2= st.columns(2)
        col1.metric("Tiempo", str(round(t,4)))
        col2.metric("Energia absorbida", str(round(Q,4)))
        
