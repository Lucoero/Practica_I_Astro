import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.visualization import quantity_support
import re

quantity_support()  # for getting units on the axes below  

# Nombre del fichero FITS
spec1d_file = 's0008.fits'

# Abrir el fichero
with fits.open(spec1d_file) as spec1d:
    hdu = spec1d[0]              # o hdul[1] si el espectro está en la primera extensión
    flux = hdu.data            # array de flujo 1D
    header = hdu.header        # cabecera con las palabras clave WCS
#    print(header)

# Número de píxeles del espectro
n_pix = flux.size

# Leer palabras clave WCS del eje espectral
crval1 = header["CRVAL1"]      # valor de longitud de onda en el píxel de referencia[web:4][web:9]
cdelt1 = header["CDELT1"]      # incremento de longitud de onda por píxel[web:4][web:9]
crpix1 = header.get("CRPIX1", 1.0)  # píxel de referencia (1\u2011basado); usar 1 si no existe[web:4][web:9]
obj_name = header["OBJECT"]  #Nombre de la estrella
#print(crval1,cdelt1)
#print(object)


# (Opcional) unidad y tipo de eje
cunit1 = header.get("CUNIT1", "")   # p.ej. 'Angstrom' o 'nm'[web:9]
ctype1 = header.get("CTYPE1", "")   # p.ej. 'WAVE'[web:6]

#print(data.shape)
flujo = np.ravel(flux)   # o data = data.flatten()[web:21][web:24]
#print(data.shape)

# Construir eje de longitud de onda.
# Fórmula estándar FITS: wvl = ((i + 1) - CRPIX1) * CDELT1 + CRVAL1[web:4][web:9]
pix = np.arange(n_pix)
wavelength = ( (pix + 1.0) - crpix1 ) * cdelt1 + crval1

# Función sencilla para sanear el nombre de archivo:
# deja solo letras, números, guiones, guiones bajos y puntos, sustituyendo el resto por "_".[web:68]
def sanitize_filename(s):
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', s.strip())

safe_obj = sanitize_filename(obj_name)

# Construir nombre del nuevo fichero
new_filename = f"{safe_obj}_spectrum.fits"   # p.ej. "HD000245_spectrum.fits"


# Representar el espectro
plt.figure(figsize=(8, 4))
plt.plot(wavelength, flujo, drawstyle="steps-mid")
plt.xlabel(f"Longitud de onda ({cunit1})" if cunit1 else "Longitud de onda")
plt.ylabel("Flujo")
plt.title(obj_name)
plt.tight_layout()
plt.show()

