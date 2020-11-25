import os
import functools

from randomness_testsuite.ApproximateEntropy import ApproximateEntropy as aet
from randomness_testsuite.Complexity import ComplexityTest as ct
from randomness_testsuite.CumulativeSum import CumulativeSums as cst
from randomness_testsuite.FrequencyTest import FrequencyTest as ft
from randomness_testsuite.BinaryMatrix import BinaryMatrix as bm
from randomness_testsuite.Matrix import Matrix as mt
from randomness_testsuite.RandomExcursions import RandomExcursions as ret
from randomness_testsuite.RunTest import RunTest as rt
from randomness_testsuite.Serial import Serial as serial
from randomness_testsuite.Spectral import SpectralTest as st
from randomness_testsuite.TemplateMatching import TemplateMatching as tm
from randomness_testsuite.Universal import Universal as ut



path_to_input = './maximos_DATA_20190307-0003_4_10Millones.bin-20201008T145227Z-001/maximos/binarizacion'





test_function = {
    0:ft.monobit_test,
    1:ft.block_frequency,
    2:rt.run_test,
    3:rt.longest_one_block_test,
    4:mt.binary_matrix_rank_text,
    5:st.sepctral_test,
    6:tm.non_overlapping_test,
    7:tm.overlapping_patterns,
    8:ut.statistical_test,
    9:ct.linear_complexity_test,
    10:serial.serial_test,
    11:aet.approximate_entropy_test,
    12:cst.cumulative_sums_test,
    13:functools.partial(cst.cumulative_sums_test, mode=1),
    14:ret.random_excursions_test,
    15:ret.variant_test
}

all_results = {}
for dirpath,dirname, files in os.walk(path_to_input):#Direcion de los archivos binarizados
    for archivo in files:
        print(archivo)
        input_file = open(os.path.join(path_to_input,archivo), 'r')#Direcion de los archivos binarizados
        data = input_file.read()
        results = []
        for test in test_function.values():
            results.append(test(data))
        all_results[f'{archivo}']= results

output = "Archivo;01. Frequency Test (Monobit);02. Frequency Test within a Block;03. Run Test;04. Longest Run of Ones in a Block;05. Binary Matrix Rank Test;06. Discrete Fourier Transform (Spectral) Test;07. Non-Overlapping Template Matching Test;08. Overlapping Template Matching Test;09. Maurer\s Universal Statistical test;10. Linear Complexity Test;11. Serial test;12. Approximate Entropy Test;13. Cummulative Sums (Forward) Test;14. Cummulative Sums (Reverse) Test;15. Random Excursions Test;16. Random Excursions Variant Test\n"

for result in all_results.keys():
    resultados = f"{result}"
    for rr in all_results[result]:
        resultados += f";{rr}"
    output += resultados + "\n"

output_file = open(f'resultados2.csv', 'w')
output_file.write(output)
output_file.close()