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
import math

def main():

    # VARIABLES
    BUFFER_DEL_PUNTO = 4

    # columnas
    # ID,PARCELA,X,Y,TIPO

    # path archivos csv
    path_archivos_csv = "/home/jorge/Documents/Research/procesamiento_raster/data"

    #path_leer_archivo
    path_archivo_puntos = "/home/jorge/Documents/Research/procesamiento_raster/coordenadas.csv"

    # variable de archivos
    lista_de_archivos = [x for x in os.listdir(path_archivos_csv) if x.endswith('_pp.csv')]

    # dataFrame puntos
    df_puntos = pd.read_csv(path_archivo_puntos)

    # ciclo de puntos
    primer_ciclo = True

    # array columnas

    cols = ["x", "y", "ID", "PARCELA", "TIPO"]

    for index, row in df_puntos.iterrows():

        x = row["x"]
        y = row["y"]
        numero = row["ID"]
        parcela = row["PARCELA"]
        tipo = row["TIPO"]

        # ciclo for
        for i in lista_de_archivos:
            nombre_archivo, extension = i.split(".")
            ruta_del_archivo = "{}/{}".format(path_archivos_csv, i)

            # generar nombre de la variable
            nombre_variable, extension2 = nombre_archivo.split("_pp")
            print(nombre_variable)

            # leer archivo a procesar
            data = pd.read_csv(ruta_del_archivo)

            # generar xi, yi, xf, yf
            xi = x - BUFFER_DEL_PUNTO
            yi = y - BUFFER_DEL_PUNTO

            xf = x + BUFFER_DEL_PUNTO
            yf = y + BUFFER_DEL_PUNTO

            # acotar el área de procesamiento
            data = data.loc[data["x"] >= xi]
            data = data.loc[data["x"] <= xf]

            data = data.loc[data["y"] >= yi]
            data = data.loc[data["y"] <= yf]

            data["ID"] = numero
            data["PARCELA"] = parcela
            data["TIPO"] = tipo

            #data["x"] = data["x"].astype(int)
            #data["y"] = data["y"].astype(int)

        #    print("data",data.head())

            # nombre archivo procesado
            nombre_archivo_exportar = "/home/jorge/Documents/Research/procesamiento_raster/resultados/{}_{}_{}_{}.csv".format(nombre_variable, numero, parcela, tipo)
            data.to_csv(nombre_archivo_exportar, index=False)

if __name__ == '__main__':
    main()
