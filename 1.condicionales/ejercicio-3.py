"""
Un almacén de venta de ropa tiene las siguientes promociones para sus clientes,
las cuales consisten en lo siguiente
(pago en efectivo = 1, pago con Tarjeta de Crédito = 2):

    a. Para ventas menores ó iguales a 100.000, con pago en efectivo,
        se hace un descuento del 20% y si es con tarjeta de crédito, se hace el 10%.
    b. Para ventas mayores a 100.000 y menores o iguales a 200.0000, con pago
        en efectivo, se hace un descuento del 30%, con tarjeta de crédito se hace el 15%.
    c. Para ventas mayores a 200.000, con pago en efectivo, se hace un descuento del 40% y
        con tarjeta de crédito se hace el 20%. Indique el valor del descuento y el
        total a pagar.
"""
monto = 0.0
print("")
print("Presione 1 para comprar el articulo y 2 para no comprarlo"
      "\n -------------------------------------------"
      "\n|  Articulos de compra  |      Precio      |"
      "\n -------------------------------------------")
aux = int(input("| => Polo               |       30.5       | >> "))
if aux == 1: monto += 30.5
aux = int(input("| => Falda              |       43.7       | >> "))
if aux == 1: monto += 43.7
aux = int(input("| => Short              |       25.0       | >> "))
if aux == 1: monto += 25.0
aux = int(input("| => Gorro              |       15.5       | >> "))
if aux == 1: monto += 15.5
aux = int(input("| => Zapatilla          |      102.84      | >> "))
if aux == 1: monto += 102.84
aux = int(input("| => Vestido            |       98.6       | >> "))
if aux == 1: monto += 98.6
aux = int(input("| => Polera             |       55.9       | >> "))
if aux == 1: monto += 55.9

print(" -------------------------------------------")

print("")
print(f'El monto total a pagar sin el descuento es {monto}')
print("")
print(" -------------------------------------------"
      "\n|   ¿Con que medio desea realizar el pago   |"
      "\n -------------------------------------------"
      "\n| 1. Pago en efectivo                       |"
      "\n| 2. Pago con tarjeta de crédito            |"
      "\n -------------------------------------------"
     )
aux = int(input('>>> Opcion: '))
descuento = float()

""" SACAR EL MONTO A PAGAR DIRECTAMENTE (no hay necesidad de la variable 'decuento')
if aux == 1:
    if monto <= 100.000: monto *= 0.8
    elif monto <= 200.000: monto *= 0.7
    else: monto *= 0.6
elif aux == 2:
    if monto <= 100.000: monto *= 0.9
    elif monto <= 200.000: monto *= 0.85
    else: monto *= 0.8

print(f'\nEl monto a pagar es {monto}')
"""
if aux == 1:
    if monto <= 100.000: descuento = monto * 0.2
    elif monto <= 200.000: descuento = monto * 0.3
    else: descuento = monto * 0.4
elif aux == 2:
    if monto <= 100.000: descuento = monto * 0.1
    elif monto <= 200.000: descuento = monto * 0.15
    else: descuento = monto * 0.2

print(f'\nEl descuento es de {descuento} y el monto final a pagar es {monto - descuento}')
