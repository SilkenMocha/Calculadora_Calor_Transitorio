import math
import streamlit as st
import pandas as pd
import numpy as np
import math
#___________________
from scipy.integrate import quad

def placa():

    def f(x):
        return x*(1-x)

    def integrand(n, x):
        return f(x)*np.sin(n*np.pi*x)

    def calculate_lambda(n):
        return quad(integrand, 0, 1, args=(n,))[0]

    n_values = np.arange(1, 11)

    for n in n_values:
        lambda_n = calculate_lambda(n)
        st.write(f"Lambda_{n} = {lambda_n}")
