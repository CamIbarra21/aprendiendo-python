# F U N C I O N E S
"""
Permiten definir algún tipo de algoritmo que va a ser utilizado
constantemente en el desarrollo de un proyecto, de modo que,
pueda reducirce líneas de código
"""
def suma(a,b):
    resultado = a + b
    return resultado

def resta(a,b):
    resultado = a - b
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division(a,b):
    resultado = a / b
    return resultado

def modulo(a,b):
    resultado = a % b
    return resultado

# F U N C I O N   R E C U R S I V A
"""
Es una función que se llama a si misma y se repite constantemente
hasta cumplir una condición de parada, caso contrario, se repite
de manera indefinida
"""
def potencia(a,b):
    if b == 1:
        return a
    elif b == 0:
        a = 1

    return a * potencia(a,b - 1)

# L A M B D A
"""
Es una forma más corta y sencilla de escribir funciones, caracterizadas
por ser pequeñas y anónimas. Solo pueden utilizarce en la función de
orden superior a la que pertenecen
"""

sumaLambda = lambda a,b: (a + b)
restaLambda = lambda a,b: (a - b)
multiplicacionLambda = lambda a,b: (a * b)
divisionLambda = lambda a,b: (a / b)
moduloLambda = lambda a,b: (a % b)
potenciaLambda = lambda a,b: (pow(a,b))

n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese otro numero: '))
print(f"\nSuma: {sumaLambda(n1,n2)}"
      f"\nResta: {resta(n1,n2)}"
      f"\nMultiplicación: {multiplicacionLambda(n1,n2)}"
      f"\nDivisión: {division(n1,n2)}"
      f"\nMódulo: {moduloLambda(n1,n2)}"
      f"\nPotencia: {potencia(n1,n2)}"
      )