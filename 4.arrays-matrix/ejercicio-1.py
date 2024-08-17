"""
Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y crear una función 
que rellene el array o arreglo con los múltiplos de un número pedido por teclado. 
Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la función, 
el array contendrá 3, 6, 9, 12, 15. Muestralos por pantalla usando otra función distinta.
"""

def imprimirArreglo(arr, factor):
    i = 1
    for elemento in arr:
        print(f'{i} * {factor} = {elemento}')
        i += 1


tamanio = int(input('Ingrese el tamaño del arreglo: '))
factor = int(input('Ingrese el número base del que se hallaran los multiplos: '))
arreglo = []

for i in range(tamanio):
    arreglo.append((i + 1) * factor)

imprimirArreglo(arreglo, factor)