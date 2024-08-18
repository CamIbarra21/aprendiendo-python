from operations import *
from print_matrix import *

matrizA = [[1, 2, 3, 4],
           [6, 7, 8, 9],
           [6, 7, 8, 9]]

matrizB = [[9, 8, 7, -1],
           [5, 9, 5, 2],
           [1, 3, 3, 2],
           [1, 4, -3, 2]]
matrizC = [[6, 1, 1],
           [4, -2, 5],
           [2, 8, 7]]

validMatrix = lambda matrix: (len(matrix) > 1 and len(matrix[0]) > 1)

matrizResultado = addition(matrizA, matrizB)
if validMatrix(matrizResultado):
    printMatrix(matrizResultado)
else:
    print('Suma no valida')
print("")

matrizResultado = multiplication(matrizA, matrizB)
printMatrix(matrizResultado)
#matrizResultadoResta = subtraction(matrizA, matrizB)
#print("\nEl resultado es: ", matrizResultadoResta)
print("")
determinante = determinant(matrizA)
if determinante == 'ERROR':
    print('No es posible calcular la determinante de esta matriz')
else:
    print('La determinante de la matriz es ', determinante)

matrizResultado = transpose(matrizB)
printMatrix(matrizResultado)