# -*- coding: utf-8 -*-
"""
Practica 3
"""
#%% Librerias
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate


import Load_Data as LD
import Show_Spectra as SSp
import parametros as Par
import Herramientas as Herr
import normalizar as Norm
#%% Variables entrada

medB = ".fits"
bigB = ".fits"

lines = {} # Escogemos las que se vean bien

#%% Proceso principal

medFlux, medLamb = LD.Load_Miles(medB)
bigFlux,bigLamb = LD.Load_Miles(bigB)

# Los ploteamos para verlos
SSp.Compare_Spectra([medFlux,bigFlux],[medLamb,bigLamb], TArr = ["Estrella 1", "Estrella 2"], title = "Estrellas Escogidas", lines = lines)

# Normalizamos

# Vemos normalizaciones

# Aislamos las lineas que queremos y las aproximamos


