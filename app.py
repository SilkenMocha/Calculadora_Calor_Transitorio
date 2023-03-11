import streamlit as st
import numpy as np
import pandas as pd
#___________________________________
import parametros_concentrados as pc
#import newton as nw
#import secante as sc
#import regulafalsi as fp
#import cramer as cr
from PIL import Image

st.title ("Transferencia de Calor")
#image = Image.open('metodos.jpg')
#st.image(image)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Calculadora de calor transitorio")
with col2:
    st.subheader("Erick López - 348916")

#Parámetros Concentrados, Placa, Cilindro, Esfera, Sólido Semiinfinito.

seleccion = st.selectbox("Seleccione una opción: ", ["Parámetros Concentrados", "Placa", "Cilindro", "Esfera", "Sólido Semiinfinito"])

if seleccion == "Parámetros Concentrados": 
    st.subheader("Parámetros Concentrados")
    #st.latex('''x^3 - 6x^2 + 11x -6.1''')
    pc.parametros_concentrados()

if seleccion == "Placa": 
    st.subheader("Placa")
    col1, col2 = st.columns(2)
    with col1:
        st.latex('''x^3 - 6x^2 + 11x -6.1''')
    
    with col2:
        st.latex('''\dfrac {\mathrm{d}}{\mathrm{d} x}= 3x^2-12x+11''')
    #nw.newton()

if seleccion == "Cilindro": 
    st.subheader("Cilindro")
    #st.latex('''x^3 - 6x^2 + 11x -6.1''')
    #sc.secante()

if seleccion == "Esfera": 
    st.subheader("Esfera")
    #st.latex('''x^3 - 6x^2 + 11x -6.1''')
    #fp.regulafalsi()

if seleccion == "Sólido Semiinfinito": 
    st.subheader("Sólido Semiinfinito")
    #with col1:
        #st.latex('''x + y = 1''')
    #with col2:
        #st.latex('''x + 5y = 10''')
        
    #A = np.array([ [1,1], [1,5]])
    #b = np.array([1,10])

    #cr.cramer(A,b)
    
    #image = Image.open('ratoncito.jfif')
    #st.image(image, width = 400, caption = "Gracias por su atención")
