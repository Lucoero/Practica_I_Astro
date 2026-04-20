
import numpy as np

import normalizar
from parametros import *
import Herramientas



def puta(f,p,d):
    aux = np.zeros(len(f))
    for i in range(len(p)):
        a = p[i] - d
        b = p[i] + d
        lsup = f[b]
        linf = f[a]
        pe = (lsup - linf)/(2*d)
        for t in range(a,b+1):
            aux[t] = linf + pe*(t-a)
    for j in range(len(f)):
        if aux[j] == 0:
            aux[j] = f[j]
    return aux




def hola(wave,flux,lines, d = 15):
    pks = picos(wave,flux,lineas,15)
    rr = puta(flux,pks,d)
    norm = flux/rr
    return norm
