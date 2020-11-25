# -*- coding: utf-8 -*-
from pytisean import tiseanio
import matplotlib.pyplot as plt
import numpy as np
import time

 
def test_fv(datos, dimension_min=1, dimension_max= 20):
    """
    Funcion para detectar la dimension de embeding usando los falsos primeros vecinos
    La proporcion de primeros vecinos la calcula automaticamente con tisean,
    luego revisa si la proporcion es suficientemente baja para considerarla que llega a 
    la dimensionde embedding 
    Input:
        datos: serie temporal
        dimension_min = dimension minima
        dimension_max = dimension maxima
    Output:
        falsosv: matriz que devuelve tisean, cada fila es un calculo para una dimension,
             las columnas son [dimension, fraccion de falsos primeros vecinos, ...]
        caotico: booleano que indica si se encontro una dimension de embedding
        i+1: la dimension de embedding
    """
    falsosv, msg = tiseanio('false_nearest', '-d1',f'-m{dimension_min}',f'-M1,{dimension_max}' ,'-V2', data=datos)
    caotico = False
    neecsito_ver_mas = True
    fv_anterior = 100
    for i in range(len(falsosv[:,1])):
        if falsosv[i,1] < 0.01:
            caotico = True
            neecsito_ver_mas = False
            break
        else:
            if fv_anterior == 100:
                fv_anterior = falsosv[i,1]
            else:
                variacionfv = 1 - falsosv[i,1]/fv_anterior
                if variacionfv < -0.1:
                    caotico = False
                    neecsito_ver_mas = False
                    break
                elif variacionfv < 0.01 and falsosv[i,1] <= 0.05:
                    caotico = True
                    neecsito_ver_mas = False
                    break
                fv_anterior = falsosv[i,1]
    return falsosv,caotico,neecsito_ver_mas,i+1