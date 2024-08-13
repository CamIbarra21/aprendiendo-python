#Convertir un numero entero de 3 cifras o menos a romano
num = int(input('Ingrese un numero: '))
c = num // 100
d = (num % 100) // 10
u = num % 10

#print('Cen: ', c, '\nDec: ', d, '\nUni: ', u, '\n')

print("")
romano = str()

if(c == 9): romano+='CM'
elif(c == 8): romano+='DCCC'
elif(c == 7): romano+='DCC'
elif(c == 6): romano+='DC'
elif(c == 5): romano+='D'
elif(c == 4): romano+='CD'
elif(c == 3): romano+='CCC'
elif(c == 2): romano+='CC'
elif(c == 1): romano+='C'

if(d == 9): romano+='XC'
elif(d == 8): romano+='LXXX'
elif(d == 7): romano+='LXX'
elif(d == 6): romano+='LX'
elif(d == 5): romano+='L'
elif(d == 4): romano+='XL'
elif(d == 3): romano+='XXX'
elif(d == 2): romano+='XX'
elif(d == 1): romano+='X'

if(u == 9): romano+='IX'
elif(u == 8): romano+='VIII'
elif(u == 7): romano+='VII'
elif(u == 6): romano+='VI'
elif(u == 5): romano+='V'
elif(u == 4): romano+='IV'
elif(u == 3): romano+='III'
elif(u == 2): romano+='II'
elif(u == 1): romano+='I'

print(f'El numero {num} en romanos es {romano}')