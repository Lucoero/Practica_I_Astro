# -*- coding: utf-8 -*-
"""
Show_Spectra

Dado los arrays de datos, ploteamos los espectros con distintas propiedades
"""

import numpy as np
import matplotlib.pyplot as plt


def Blank_Spectra(lamb,flux, title = "Espectro", onlyObject = False):
    """
    Blank_Spectra:
        
        Ploteamos el espectro con la menor cantidad de cambios posible.
        Perfecto para un primer acercamiento
    """
    fig, ax = plt.subplots(figsize = (15,6))
    fig.suptitle(title)
    ax.set_xlabel(r"$\lambda \ (A^{\circ})$")
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
    minLine = np.min(flux)*10
    maxLine = np.max(flux)*10
    # Ploteamos las lineas
    for name in lines:
        ax.vlines(lines[name], minLine,maxLine )
    fig.show()
    return

def Compare_Spectra():
    """
    Co
    """
