import math

n1 = float(input('Ingrese un numero: '))
n2 = float(input('Ingrese otro numero: '))

#potencia = n1**3
print(f'Suma > {n1 + n2}')
print(f'Resta > {n1 - n2}')
print(f'Mult > {n1 * n2}')
print(f'Divi > {n1 / n2}')
print(f'Div > {n1 // n2}')
print(f'Mod > {n1 % n2}')
print("Pote >", (n1**2))

print("")
print("***")
print("")

print("= = = LIBRERIA MATH = = =")
n3 = float(input('Ingrese un numero: '))
raiz = math.sqrt(n3)
print(f'Raiz de {n3} = {raiz}')

#Separar parte entera y decimal de la raiz calculada
print(f'Parte entera --> {round(raiz)}')
print(f'Parte decimal --> {raiz - round(raiz)}')