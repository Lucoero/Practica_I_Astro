


import normalizar
import parametros
import Herramientas



def puta(l,f,p,d):
    aux = np.zeros(len(f))
    for i in p:
        a = i - d
        b = i + d
        lsup = f[b]
        linf = f[a]
        pe = (lsup - linf)/(2*d)
        for t in range(a,b+1):
            aux[t] = linf + pe*(t-a)
    for j in range(len(f)):
        if aux[j] == 0:
            aux[j] = f[j]
    return aux
