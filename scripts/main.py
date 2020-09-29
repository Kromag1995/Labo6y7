import numpy as np
import os
from complejidad import complejidad
from bin_media import bin_media
from bin_mediana import bin_mediana


"Complejidad de V"
for dirpath,dirname, files in os.walk('./maximos'):
    for archivo in files:
        if ('V' in archivo):
            maximos = np.loadtxt(dirpath+'/'+archivo)
            binarios_media = bin_media(maximos)
            binarios_mediana = bin_mediana(maximos)
            print(archivo)
            print("Complejidad media: ",complejidad(binarios_media))
            print("Complejidad mediana: ",complejidad(binarios_mediana))
            del(maximos)
            del(binarios_media)
            del(binarios_mediana)

"Complejidad de t"
for dirpath,dirname, files in os.walk('./maximos'):
    for archivo in files:
        if ('t' in archivo):
            maximos_temp = np.loadtxt(dirpath+'/'+archivo)
            def_temp = []
            for i in range(1,len(maximos_temp)):
                def_temp.append(maximos_temp[i]-maximos_temp[i-1])
            binarios_media = bin_media(def_temp)
            binarios_mediana = bin_mediana(def_temp)
            print(archivo)
            print("Complejidad media: ",complejidad(binarios_media))
            print("Complejidad mediana: ",complejidad(binarios_mediana))
            del(maximos_temp)
            del(def_temp)
            del(binarios_media)
