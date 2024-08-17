"""
    Diseñe un programa que lea un vector y calcule si hay un numero que
    sea igual a la suma de los demas elementos del vector
"""
vector = []
suma = 0
existeVector = False

tamanio = int(input('Ingrese el tamaño del vector: '))

for i in range(-1, tamanio):
    if i != -1:
        nuevo = int(input(f'Ingrese el elemento {i} del vector: '))
        vector.append(nuevo)
        suma += vector[i]
    else:
        numero = int(input('Ingrese el numero de la posible suma del resto de elemento del vector: '))

if numero == suma:
    print(f'La suma de los elementos del vector existe y es {suma}')
else:
    print('El numero ingresado no es la suma de los elementos del vector')