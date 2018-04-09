#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Script que permite la generación de
# archivo csv a partir de valores de raster
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################
Created on Mon Jul 17 16:17:25 2017
@author: jorgemauricio
"""

# librerias
import pandas as pd
import numpy as np
import os

# main
def main():

    # path
    path_guardar_archivo = "/home/jorge/Documents/Research/procesamiento_raster/data"
    path_leer_archivo = "/media/jorge/backup1/Magali"

    # variable de archivos
    lista_de_archivos = [x for x in os.listdir(path_leer_archivo) if x.endswith('.xyz')]

    for i in lista_de_archivos:

        nombre_archivo, extension = i.split(".")

        ruta_del_archivo = "{}/{}".format(path_leer_archivo, i)

        # leer archivo
        data = pd.read_table(ruta_del_archivo, sep="\s+", header=None)

        # variable de columnas
        cols = ["x","y", nombre_archivo]

        # asignar columnas
        data.columns = cols

        # delimitar valores de x
        data = data.loc[data["x"] >= 672496]

        # delimitar valores de y
        data = data.loc[data["y"] >= 2834425]

        # delimitar valores de índice
        data = data.loc[data[nombre_archivo] >= 0]

        nombre_archivo_exportar = "{}/{}_pp.csv".format(path_guardar_archivo, nombre_archivo)
        data.to_csv(nombre_archivo_exportar, index=False)

        print(nombre_archivo_exportar)

# if
if __name__ == '__main__':
    main()
