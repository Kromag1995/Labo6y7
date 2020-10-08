import numpy as np
from scipy.signal import find_peaks
import os

if "maximos" in os.listdir():
    os.mkdir("maximos")
datos=[]
for dirpath,dirname, files in os.walk('./datos'):
    for archivo in files:
        if ('.bin' in archivo):
            datos = open(dirpath+'/'+archivo)
            #convierto los datos a float
            tira = np.fromfile(datos,dtype=float)
            salto=102.4*(1e-9)
            tiempos = np.arange(0,salto*len(tira),salto)

            filtrado_V=[]
            filtrado_t=[]
            count_inf = 0
            for i in range(len(tira)):
                if tira[i] > 0.001:
                    if tira[i] == np.inf:
                        count_inf += 1    
                    else:
                        filtrado_V.append(tira[i])
                        filtrado_t.append(tiempos[i])
            maximos_V=[]
            maximos_t=[]
            peaks, _ = find_peaks(filtrado_V,height=0.05,distance = 15)
            for i in peaks:
                    maximos_V.append(filtrado_V[i])
                    maximos_t.append(filtrado_t[i])
            print(f'La cantidad de picos saturados es {count_inf} de {len(maximos_V)} de datos')
            print(f'Esto representa %{count_inf*100/len(maximos_V)} de tus datos')
            print(f'La cantidad de picos saturados es {count_inf} de {len(filtrado_V)} de datos')
            print(f'Esto representa %{count_inf*100/len(filtrado_V)} de tus datos')
            archivo = archivo.replace(".bin","")
            np.savetxt(f"./maximos/Nobinzarizados/{archivo}_maximos_V",maximos_V)
            np.savetxt(f"./maximos/Nobinzarizados/{archivo}_maximos_t",maximos_t)
            del(datos)
            del(tira)
            del(filtrado_t)
            del(filtrado_V)
            del(maximos_t)
            del(maximos_V)
            del(peaks)
            del(tiempos)