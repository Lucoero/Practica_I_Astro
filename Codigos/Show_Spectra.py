# -*- coding: utf-8 -*-
"""
Show_Spectra

Dado los arrays de datos, ploteamos los espectros con distintas propiedades
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Variables globales de plots
yscale = 1.01 # Escala para escoger el tamanno de los plots
linewidth = 1 # Grosor de las lineas de plot
#%% Funciones
def Blank_Spectra(lamb,flux, title = "Espectro", onlyObject = False):
    """
    Blank_Spectra:
        
        Ploteamos el espectro con la menor cantidad de cambios posible.
        Perfecto para un primer acercamiento
    """
    fig, ax = plt.subplots(figsize = (15,6))
    fig.suptitle(title)
    ax.set_xlabel(r"$\lambda \ (\mathring{A})$")
    ax.set_ylabel("Flujo (unidades arbitrarias)")
    ax.plot(lamb,flux, linewidth = 1)
    if onlyObject:
        return fig,ax # Devuelvo los ejes sin plottear
    fig.show()
    return

def Lined_Spectra(lamb,flux,lines, title = "Lined_Spectra"):
    """
    Lined_Spectra:
        Ploteamos el espectro con las lineas que queramos marcar.
        Lines debe enviarse como un diccionario con {"line_name" : lamb,}
    """
    # Ploteamos espectro
    fig,ax = Blank_Spectra(lamb, flux, title = title, onlyObject = True)
    minLine = np.min(flux)*yscale
    maxLine = np.max(flux)*yscale
    # Ploteamos las lineas
    for name in lines:
        ax.vlines(lines[name], minLine,maxLine )
    fig.show()
    return

def Compare_Spectra(lamb1,flux1,lamb2,flux2,lines = {}, title = "Comparison between Spectras"):
    """
    Compare_Spectra:
        Ploteamos uno al lado del otro dos espectros para compararlos. Si se dan lineas
        como parametro opcional, las coloca tambien en ambos
    """
    fig,ax = plt.subplots(2,1, figsize = (60,6),sharex=True, sharey=False)
    ax[1].set_xlabel(r"$\lambda\ (\mathring{A})$")
    
    ax[1].set_ylabel("Flujo (uds arbitrarias)")
    ax[0].set_ylabel("Flujo (uds arbitrarias)")
    
    ax[0].set_title("Spectra 1")
    ax[1].set_title("Spectra 2")
    
    #Ploteamos los espectros
    ax[0].plot(lamb1,flux1,linewidth = 1)
    ax[1].plot(lamb2,flux2,linewidth = 1)
    
    # Ploteamos las lineas
    minLine = np.min((flux1,flux2))*yscale
    maxLine = np.max((flux1,flux2))*yscale
    
    ax[0].set_ylim(minLine,maxLine)
    ax[1].set_ylim(minLine,maxLine)
    for name in lines:
        ax[0].vlines(lines[name], minLine,maxLine, color = "red")
        ax[1].vlines(lines[name], minLine,maxLine, color = "red")
    fig.show()
    return
    