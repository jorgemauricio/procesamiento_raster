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
    # path archivos csv
    path_archivos_csv = "/home/jorge/Documents/Research/procesamiento_raster/resultados"

    #path_leer_archivo
    path_archivo_compilado = "/home/jorge/Documents/Research/procesamiento_raster/compilado.csv"

    # variable de archivos
    lista_de_archivos = [x for x in os.listdir(path_archivos_csv) if x.endswith('.csv')]

    # frames
    frames = []

    # ciclo for
    for archivo in lista_de_archivos:

        # nombre del csv a procesar
        ruta_del_archivo = "{}/{}".format(path_archivos_csv, archivo)

        # leer csv
        df = pd.read_csv(ruta_del_archivo)

        variable, dia, mes, anio, identificador, parcela, tipo = procesamiento_variables(archivo)

        df["variable"] = variable
        df["dia"] = int(dia)
        df["mes"] = int(mes)
        df["anio"] = int(anio)
        df["identificador"] = int(identificador)
        df["parcela"] = int(parcela)
        df["tipo"] = tipo

        nombre_variable = "{}_{}_{}_{}".format(variable, complemento_dia(dia), mes, anio)

        df["valor"] = df[nombre_variable]

        df = df[['x', 'y', 'ID', 'PARCELA', 'TIPO', 'variable',
       'dia', 'mes', 'anio', 'identificador', 'parcela', 'tipo', 'valor']]

        frames.append(df)

    data = pd.concat(frames)

    # save csv
    data.to_csv(path_archivo_compilado)
    
def procesamiento_variables(arr):
    # procesamiento de variables
    arreglo_temporal = arr.split(".")

    arreglo_variables = arreglo_temporal[0].split("_")

    print(arreglo_variables)
    print(len(arreglo_variables))

    var_tipo = arreglo_variables[-1]

    var_parcela = arreglo_variables[-2]

    var_id = arreglo_variables[-3]

    var_anio = arreglo_variables[-4]

    var_mes = arreglo_variables[-5]

    var_dia = arreglo_variables[-6]

    var_var = arreglo_variables[:-6]

    variable1 = "_".join(var_var)

    print(var_var)
    print(variable1)

    return variable1, var_dia, var_mes, var_anio, var_id, var_parcela, var_tipo

def complemento_dia(d):
    if d == 3 or d == 9:
        dia_texto = "0{}".format(d)
        return dia_texto
    else:
        return d

if __name__ == '__main__':
    main()
