import random

# F O R   E A C H
"""
Se utiliza mas comunmente con estructuras como listas y tuplas.
En esta seccion se utiliza para iterar cada caracter en un string
"""
nombre = "Camila Ibarra"

for letra in nombre:
    print(letra)

# F O R
"""
Una forma más básica del foreach que itera segun una condicional 
y no segun los elementos que hay una estructura de por si
"""
rango_min = 5 #es inclusivo en el for ( <= )
rango_max = 10 #es excluyente en el for ( > )
salto = 2
for i in range(rango_max):
    print(f'Prueba sin min {i}')

print("")

for i in range(rango_min, rango_max):
    print(f'Prueba con min {i}')

print("")

for i in range(rango_min, rango_max, salto):
    print(f'Prueba con salto {i}')

# W H I L E
"""
Es una estructura repetitiva que requiere de una condicional para detenerse
"""
contador = 0
while contador < 10:
    contador+=1
    print(f'Contador en {contador}')

print("")

numCorrecto = False
aleatorio = random.randrange(0,100)

while not numCorrecto:
    numero = int(input('Ingrese un numero entero entre el 0 y el 100: '))
    if numero < aleatorio: print("-> El numero que ingresaste es menor")
    elif numero > aleatorio: print("-> El numero que ingresaste es mayor")
    else: numCorrecto = True
print(f'\n* * * Hallaste el numero aleatorio {aleatorio} * * *')
