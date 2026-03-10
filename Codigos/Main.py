# -*- coding: utf-8 -*-
"""
Main
"""
import numpy as np
import matplotlib.pyplot as plt
import Load_Data as LD
import Show_Spectra as SSp

plt.close("all")
#%% Variables de llamada
Prob_Name = "estrella4.dat"
Miles_Name = "s0010.fits"
#%% Obtencion de datos

PLamb, PFlux = LD.Load_Dat(Prob_Name)

#MLamb,MFlux = LD.Load_Miles(Miles_Name)
#%% Correcciones
#%% Ploteado

SSp.Blank_Spectra(PLamb,PFlux)
#SSp.Blank_Spectra(MLamb, MFlux)