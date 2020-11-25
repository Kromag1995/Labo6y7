import numpy as np
from scipy.signal import find_peaks
import os

datos=[]
for dirpath,dirname, files in os.walk('/home/dell/Documents/Labo 6/data/Muestras sin saturacion'):
    for archivo in files:
        if ('DATA_20190307-0003_4_10Millones.bin' in archivo):
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
            altura=[0.1, 0.06,0.05,0.04,0.03,0.02,0.01]
            for j in range(len(altura)):
                peaks, _ = find_peaks(filtrado_V,height = altura[j] ,distance = 15)
                for i in peaks:
                    maximos_V.append(filtrado_V[i])
                    maximos_t.append(filtrado_t[i])
                print(f'La cantidad de picos saturados es {count_inf} de {len(maximos_V)} de maximos en med {archivo}')
                print(f'Esto representa %{count_inf*100/len(maximos_V)} de tus datosen med {archivo}')
                print(f'La cantidad de picos saturados es {count_inf} de {len(filtrado_V)} de datos totales en med {archivo}')
                print(f'Esto representa %{count_inf*100/len(filtrado_V)} de tus datos en med {archivo}')
                if not os.path.isdir(f'maximos_{archivo}'):
                    os.mkdir(f'maximos_{archivo}')
                if not os.path.isdir(f'./maximos_{archivo}/Nobinzarizados'):
                    os.mkdir(f'./maximos_{archivo}/Nobinzarizados')
                np.savetxt(f"./maximos_{archivo}/Nobinzarizados/{archivo} maximos_V_{altura[j]}",maximos_V)
                np.savetxt(f"./maximos_{archivo}/Nobinzarizados/{archivo} maximos_t_{altura[j]}",maximos_t)
            del(datos)
            del(tira)
            del(filtrado_t)
            del(filtrado_V)
            del(maximos_t)
            del(maximos_V)
            del(peaks)
            del(tiempos)
