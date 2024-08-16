"""
    Solicitar al usuario que ingrese números enteros positivos y, por cada uno,
    imprimir la suma de los dígitos que lo componen. 
    La condición de corte es que se ingrese el número -1. 
    Al finalizar, mostrar cuántos de los números ingresados por el usuario 
    fueron números pares.
"""
contPares = 0
detener = False

while not detener:
    numero = int(input('\nIngrese un numero entero positivo: '))
    if numero == -1:
        detener = True
    elif numero < 0:
        print('El número tiene que ser positivo')
    else:
        suma = 0
        if numero % 2 == 0 and numero != 0:
            contPares += 1
        while numero > 0:
            suma += (numero % 10)
            numero //= 10
        print(f'La suma de los digitos del numero es {suma}')
        
print(f'\n* * * Se ha ingresado exitosamente {contPares} numeros pares * * *')