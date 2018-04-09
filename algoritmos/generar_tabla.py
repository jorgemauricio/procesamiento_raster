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

def main():
    # path
    path = "/home/jorge/Documents/Research/procesamiento_raster/data"

    # variable de archivos
    lista_de_archivos = [x for x in os.listdir(path) if x.endswith('.csv')]

    # variable primer archivo
    primer_ciclo = True

    # ciclo for
    for i in lista_de_archivos:
        nombre_archivo, extension = i.split(".")
        ruta_del_archivo = "{}/{}".format(path, i)

        nombre_variable, extension2 = nombre_archivo.split("_pp")
        print(nombre_variable
        )
        data = pd.read_csv(ruta_del_archivo)

        if primer_ciclo:
            dataFinal = data
            primer_ciclo = False
        else:
            dataFinal[nombre_variable] = data[nombre_variable]

    ruta_del_archivo_final = "{}/archivo_procesado.csv".format(path)
    dataFinal.to_csv(ruta_del_archivo_final)

if __name__ == '__main__':
    main()
