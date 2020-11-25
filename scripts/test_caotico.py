import os
import numpy as np
from falsos_vecinos import test_fv
import matplotlib.pyplot as plt
from lyapunov import lyapunov

"""
Script para calcular la dimension de embedding utilizando primeros vecinos y
luego calcular los exponentes de lyapunov para determinar la caoticidad del sistema
"""



input_path = './maximos/Nobinarizados/'
output_path = './falsos vecinos/'




for dirpath,dirname, files in os.walk(input_path):
    for archivo in files:
        datos = np.genfromtxt(dirpath+'/'+archivo, dtype= None)
        print(archivo)
        fv, caotico, neecsito_ver_mas, d_E  = test_fv(datos)
        if neecsito_ver_mas:
            fv, caotico, neecsito_ver_mas, d_E  = test_fv(datos,dimension_max=30)
        plt.plot(fv[:, 0], fv[:, 1]*100, '.-b')
        plt.title('False nearest neighbours d=1')
        plt.xlabel(r'Dimension', fontsize=14)
        plt.ylabel(r'False nearest neighbours (%)', fontsize=14)
        plt.grid(True)
        if caotico:
            plt.plot(fv[d_E-1,0],fv[d_E-1,1]*100, '*r')
            print("Dimension de embeding : " + str(d_E))
            lyap,paso = lyapunov(datos, d_E)
            if paso:
                print("Es Caotico")
            else:
                print("No es caotico")
            print(lyap)
        else:
            print("No es caotico")
            print("Proporcion de falsos vecinos : " + str(fv[d_E-1,1]))
        np.savetxt(output_path+archivo+"fv", fv, delimiter=',')
        np.savetxt(output_path+archivo+"lyap", lyap, delimiter=',') 
        plt.savefig(output_path+archivo+'.png', dpi=300)
        plt.clf()