print("Verificar si usted es Camila, tiene 18 años y estudia Ciencias de la Computacion")

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
carrera = str(input("Ingrese su carrera: "))

if(nombre == 'Camila' and edad == 18 and carrera == 'Ciencias de la computacion'):
    print('Acceso concedido')
else:
    print('Al menos uno de sus datos es incorrecto')

    if(nombre != 'Camila'):
        print('Su nombre es incorrecto')
    elif(edad != 18):
        print('Su edad es incorrecta')
    else:
        print('Su carrera es incorrecta')
        
    print('Acceso denegado')
