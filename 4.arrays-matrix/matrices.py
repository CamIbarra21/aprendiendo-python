# M A T R I Z
"""
Son una especie de arreglo bidimensional conformado por filas y columnas
matriz de 3 x 4
0,0     0,1     0,2     0,3
1,0     1,1     1,2     1,3    
2,0     2,1     2,2     3,3    
"""
matriz = [[4,12,6],
          [5,6,0],
          [3,8,3],
          [10,9,1]]

#Imprimir y sumar los elementos de una matriz
suma = 0
filas = 4
columnas = 3
"""
Para imprimir una matriz también funciona el método de 

for i in range(len(matriz)):
    for j in range(len(matriz)):

Aunque solo en matrices cuadradas, es decir, cuyo numero
de filas y columnas es igual
"""
for i in range(filas):
    for j in range(columnas):
        suma += matriz[i][j]
        print(matriz[i][j], end="\t")
    print("")

print(f'La suma de los elementos de la matriz es {suma}')