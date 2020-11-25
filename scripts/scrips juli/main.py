import numpy as np
import os
from complejidad import complejidad
from bin_media import bin_media
from bin_mediana import bin_mediana



#path_input='./maximos/muestras_sin_saturacion/maximos_DATA_20190307-0003_4_10Millones.bin/Nobinzarizados/'
#path_output='./maximos/muestras_sin_saturacion/maximos_DATA_20190307-0003_4_10Millones.bin/binarizados/'
path='./maximos_DATA_20190307-0003_4_10Millones.bin/'
resultados_Complejidad = "Nombre del Archivo;Longitud de la cadena;Media;Complejidad_Media(c,c/b);Mediana;Complejidad_Mediana(c,c/b) \n"
for dirpath,dirname, files in os.walk(path + 'Nobinzarizados/' ):
    for archivo in files:
        "Carga la serie de maximos de un archivo"
        maximos = np.loadtxt(dirpath+'/'+archivo)
        "Si estoy con el t de los maximos tengo que calcular la diferencia temporal"
        if ('t' in archivo):
            def_temp = []
            for i in range(1,len(maximos)):
                def_temp.append(maximos[i]-maximos[i-1])
            maximos = def_temp[:]
            del(def_temp)
        "Biniriza la serie"
        binarios_media,media = bin_media(maximos)
        binarios_mediana,mediana = bin_mediana(maximos)
        archivo = archivo.replace(".bin", "") 
        "Guarda las serie binarizadas"
        if not os.path.isdir(path +'binarizados/'):
            os.mkdir(path +'binarizados/')
        output_file = open(path +'binarizados/' + f'{archivo}_media_{len(binarios_media)}.bin', 'w')
        stingbin = ''.join([str(num) for num in binarios_media])
        output_file.write(stingbin)
        output_file.close()
        output_file = open(path + 'binarizados/' + f'{archivo}_mediana_{len(binarios_mediana)}.bin', 'w')
        stingbin = ''.join([str(num) for num in binarios_mediana])
        output_file.write(stingbin)
        output_file.close()
        "Calcula la complejidad"
        complejidad_media = complejidad(binarios_media)
        complejidad_mediana = complejidad(binarios_mediana)
        "Guarda los resultados en la string"
        resultados_Complejidad += f"{archivo};{len(binarios_media)};{media};{str(complejidad_media)};{mediana};{str(complejidad_mediana)}\n"
        "Elimina las variables que ya no usamos por cuestiones de espacio"
        del(maximos)
        del(binarios_media)
        del(binarios_mediana)


output_file = open(path + 'Resultados3.txt', 'w')
output_file.write(resultados_Complejidad)
output_file.close()
os.system('xdg-open \'\'/home/dell/Desktop/videoplayback.mp4')

