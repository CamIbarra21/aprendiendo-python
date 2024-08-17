from operations import *

matrizA = [[1, 2, 3, 4],
           [6, 7, 8, 9]]

matrizB = [[9, 8, 7, 6],
           [5, 4, 3, 2],
           [5, 4, 3, 2],
           [5, 4, 3, 2]]

matrizResultado = addition(matrizA, matrizB)
if len(matrizResultado) > 1 and len(matrizResultado[0]) > 1:
    print("\nEl resultado es: ", matrizResultado)
else:
    print('Suma no valida')

matrizResultado = multiplication(matrizA, matrizB)
print(matrizResultado)
#matrizResultadoResta = subtraction(matrizA, matrizB)
#print("\nEl resultado es: ", matrizResultadoResta)