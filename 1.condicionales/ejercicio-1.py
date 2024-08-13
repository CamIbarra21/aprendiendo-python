"""
Crear un programa en python que indique el indice de masa corporal de una persona adulta considerando que :

"El IMC es una fórmula que se calcula dividiendo el peso, expresado siempre en Kg, 
entre la altura, siempre en metros al cuadrado. Una cosa importante que destaca la 
nutricionista es que no se pueden aplicar los mismos valores en niños y adolescentes 
que en adultos. “Para calcular el IMC en niños se utilizan los percentiles. Estos 
son una media en los que se establece el peso del niño y se le relaciona con sus 
iguales de edad y sexo, dentro de la misma área; y si está en la media, tiene un 
peso adecuado; si está por encima, habría un percentil alto, por lo que  tendrían 
obesidad, y si está por debajo, se calificaría como un bajo peso”, indica Escalada.

Índice de Masa Corporal	Tu rango
15 o menos	Delgadez muy severa
15 - 15.9	Delgadez severa
16 - 18.4	Delgadez
18.5 - 24.9	Peso Saludable
25 - 29.9	Sobrepeso
30 - 34.9	Obesidad Moderada
35 - 39.9	Obesidad severa
40 o más	Obesidad muy severa (obesidad mórbida)"
Fuente: https://cuidateplus.marca.com/alimentacion/diccionario/indice-masa-corporal-imc.html
"""

import math

print('CALCULADORA DE IMC')
print("")

peso = float(input('Ingrese su peso (en kg): '))
altura = float(input('Ingrese su altura (en m): '))
imc = peso / pow(altura, 2)
resultado = 'oxo'

if(imc < 15): resultado = 'delgadez muy severa'
elif(imc < 16): resultado = 'delgadez severa'
elif(imc < 18.5): resultado = 'delgadez'
elif(imc < 25): resultado = 'peso saludable'
elif(imc < 30): resultado = 'sobrepeso'
elif(imc < 35): resultado = 'obesidad moderada'
elif(imc < 40): resultado = 'obesidad severa'
else: resultado = 'obsidad mórbida'

print("")
print(f'El valor de su MC es {imc}, por lo tanto, padece de {resultado}')