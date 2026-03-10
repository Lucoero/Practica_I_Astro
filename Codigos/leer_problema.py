#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 15:07:40 2026

@author: ignacio
"""

import re
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.visualization import quantity_support
from pathlib import Path

quantity_support()  # for getting units on the axes below  


def sanitize_filename(s):
    """Limpia string para nombre de archivo."""
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', s.strip())

# Nombre del fichero ASCII de entrada
ascii_file = "estrella4.dat"
#Ojo: Le voy a annadir al path la carpeta Estrellas_Problema
ascii_file = "Estrellas_Problema" + "/" + ascii_file
base_name = Path(ascii_file).stem

# Leer datos: saltar 3 líneas de cabecera, tabulador como separador
wavelength, flux = np.loadtxt(ascii_file, 
                              skiprows=3, 
#                              delimiter='\t', 
                              unpack=True)

print(f"Leyendo {len(wavelength)} puntos de {ascii_file}")
cunit1 = 'Angstrom'

# Representar el espectro
plt.figure(figsize=(8, 4))
plt.plot(wavelength, flux, drawstyle="steps-mid")
plt.xlabel(f"Longitud de onda ({cunit1})" if cunit1 else "Longitud de onda")
plt.ylabel("Flujo")
plt.title('Espectro')
plt.tight_layout()
plt.show()

#De regalo, vamos a crear un fits con estos datos

#new_filename= sanitize_filename(ascii_file)

#Cabecera primaria mínima (estándar VO)
primary_header = fits.Header()
primary_header['OBJECT'] = sanitize_filename(base_name)  # puedes poner otro valor
primary_header['TELESCOP'] = 'UNKNOWN'
primary_header['INSTRUME'] = 'ASCII'

# Crear columnas para FITS binary table (estándar para SPLAT-VO)
col_wave = fits.Column(name='WAVE', format='D', array=wavelength, unit='Angstrom')
col_flux = fits.Column(name='FLUX', format='D', array=flux, unit='arbitrary')


cols = fits.ColDefs([col_wave, col_flux])
hdu_table = fits.BinTableHDU.from_columns(cols)


# Crear cabecera básica con las palabras clave WCS equivalentes
n_pix = len(wavelength)
header = fits.Header()
hdu_table.header['XTENSION'] = 'BINTABLE'
hdu_table.header['NAXIS'] = 2
hdu_table.header['NAXIS1'] = 16  # tamaño de fila (2 columnas * 8 bytes)
hdu_table.header['NAXIS2'] = 1
hdu_table.header['CRVAL1'] = wavelength[0]
hdu_table.header['CDELT1'] = (wavelength[-1] - wavelength[0]) / (n_pix - 1)
hdu_table.header['CUNIT1'] = 'Angstrom'
hdu_table.header['COMMENT'] = "Espectro convertido desde ASCII a FITS"

# HDUList: primario + tabla
hdul = fits.HDUList([fits.PrimaryHDU(header=primary_header), hdu_table])

# Extensión: WAVELENGTH
header_wave = header.copy()
header_wave['EXTNAME'] = 'WAVELENGTH'
header_wave['BUNIT'] = 'Angstrom'
hdu_wave = fits.ImageHDU(data=wavelength, header=header_wave)


# Construir HDUList y nombre de salida
new_filename = f"{sanitize_filename(base_name)}_splat.fits"
hdul.writeto(new_filename, overwrite=True)
print("Escrito para SPLAT-VO:", new_filename)

