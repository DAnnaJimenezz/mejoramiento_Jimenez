# Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
# valor del medio es 11. No use operadores lógicos

def NumeroDelMedio (x,y,z):
    if x < y:
        if y < z:
            return y
    elif x < z:
        return z
    else:
        return x
    
    if x < z:
         return x
    elif y < z:
         return z
    else:
        return y

x = int (input('Ingrese el primer numero:'))
y = int (input('Ingrese el segundo numero:'))
z = int (input('Ingrese el ultimo numero:'))

numeroMedio = NumeroDelMedio (x,y,z)
print (f'El numero del medio de los tres numeros ingresados es:', {numeroMedio})