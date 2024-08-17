from operations import *
from print_matrix import *

matrizA = [[1, 2, 3, 4],
           [6, 7, 8, 9],
           [6, 7, 8, 9]]

matrizB = [[9, 8, 7, 6],
           [5, 4, 3, 2],
           [1, 4, 3, 2],
           [1, 4, 3, 2]]

validMatrix = lambda matrix: (len(matrix) > 1 and len(matrix[0]) > 1)

matrizResultado = addition(matrizA, matrizB)
if validMatrix(matrizResultado):
    printMatrix(matrizResultado)
else:
    print('Suma no valida')

matrizResultado = multiplication(matrizA, matrizB)
printMatrix(matrizResultado)
#matrizResultadoResta = subtraction(matrizA, matrizB)
#print("\nEl resultado es: ", matrizResultadoResta)