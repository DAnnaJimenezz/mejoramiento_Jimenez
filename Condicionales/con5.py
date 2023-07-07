# Escribe un programa que pida tres números y que escriba si son los tres
# iguales, si hay dos iguales o si son los tres distintos

def numerosIguales (a,b,c):
    if a == b == c:
        print ("Los tres numeros que ingreso son iguales")
    elif a == b or a == c or b == c:
        print ("Dos de los numeros ingresados por teclado son iguales")
    else:
        print ("Ninguno de los numeros son iguales")

a = int(input('Ingrese el primero numero:'))
b = int(input('Ingrese el segundo numero:'))
c = int(input('Ingrese el ultimo numero:'))

comparacion = numerosIguales(a,b,c)