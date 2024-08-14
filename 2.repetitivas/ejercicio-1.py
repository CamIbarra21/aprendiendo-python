"""
    Realizar un programa que pida al usuario la cantidad de asiatentes a una reunion, 
    pida la edad de cada asistente utilizando un for e imprima al final del programa
    el asistente con mayor y menor edad de todos
"""

cantidad = int(input('Ingrese la cantidad de asistentes a la reunion: '))

indexMen = int()
indexMay = int()
menor = int()
mayor = int()

for i in range(cantidad):

    edad = int(input(f'Edad del asistente #{i+1}: '))

    if i == 0: 
        indexMay = indexMen = 1
        menor = edad
        mayor = edad
    else:
        if edad < menor: 
            menor = edad
            indexMen = i + 1
        if edad > mayor: 
            mayor = edad
            indexMay = i + 1

print(f'El asistente #{indexMen} tiene la menor edad con {menor} años')
print(f'El asistente #{indexMay} tiene la menor edad con {mayor} años')
