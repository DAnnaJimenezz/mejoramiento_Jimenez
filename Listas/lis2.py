import random

print("LISTA 1")
def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

lista = llenarLista (10,20)
print (lista)

def sumaLista(lista):
    sum1=0
    for i in lista:
        sum1+=i
    return sum1

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayorLista(lista):
    mayor=0
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def menorLista(lista):
    menor=10000
    for i in lista:
        if i < menor:
            menor = i
    return menor

def ParesyImpares (i):
    pares1 = 0
    impares1 = 0
    if i % 2 == 0:
        pares1 += 1
    else:
        impares1 += 1
    return pares1, impares1

def cantidadParesyImpares (i):
    if i % 2 == 0:
        print (f'Cantidad de numeros pares: {cantidadParesyImpares}')
    else:
        print (f'Cantidad de numeros impares: {cantidadParesyImpares}')

print("La suma de la lista 1 es:", sumaLista(lista))
print("El promedio de la lista 1 es:", promedioLista (lista))
print ("El numero mayor de la lista 1 es:", mayorLista (lista))
print ("El numero menor de la lista 1 es:", menorLista (lista))


print ("LISTA 2")
def llenarLista2(tam,rango):
    lista2=[]
    lista2=[random.randrange(rango) for i in range(tam)]
    return lista2

lista2 = llenarLista2 (10,20)
print(lista2)

def sumaLista2(lista2):
    sum2=0
    for x in lista2:
        sum2+=x
    return sum2

def promedioLista2(lista2):
    return sumaLista2(lista2)/len(lista2)

def mayorLista2(lista2):
    mayor=0
    for x in lista2:
        if x > mayor:
            mayor = x
    return mayor

def menorLista2(lista2):
    menor=10000
    for x in lista2:
        if x < menor:
            menor = x
    return menor

def ParesyImpares2 (x):
    pares2 = 0
    impares2 = 0
    if x % 2 == 0:
        pares2 += 1
    else:
        impares2 += 1
    return pares2, impares2

def cantidadParesyImpares (x):
    if x % 2 == 0:
        print (f'Cantidad de numeros pares: {cantidadParesyImpares}')
    else:
        print (f'Cantidad de numeros impares: {cantidadParesyImpares}')
    return x

def sumaMayorListas (lista,lista2):
    sum1=sumaLista(lista)
    sum2=sumaLista2(lista2)
    if sum1 > sum2:
        print (f'La suma mayor entre las dos es lista: {sum1}')
    elif sum1 < sum2:
        print (f'La suma mayor entre las dos es lista 2: {sum2}')
    else:
        return "La suma de las dos listas son iguales"

def promedioConjunto (lista,lista2):
    sumtotal=sumaLista(lista) + sumaLista2(lista2)
    promtotal=promedioLista(lista) + promedioLista2(lista2)
    promedioConjunto = sumtotal / promtotal
    return print(f"El primedio conjunto es {promedioConjunto}")

def numpar1(lista):
    pares1=0
    for i in lista:
        if i % 2 == 0:
            pares1+=1
    return pares1

def numimpar1(lista):
    impar1=0
    for i in lista:
        if i % 2 == 1:
            impar1+=1
    return impar1


def numpar2(lista2):
    pares2=0
    for i in lista2:
        if i % 2 == 0:
            pares2+=1
    return pares2

def numimpar2(lista2):
    impar2=0
    for i in lista2:
        if i % 2 == 1:
            impar2+=1
    return impar2

def cantidadParesListas (lista,lista2):
    mayorpar=0
    if numpar1(lista) < numpar2(lista2):
        mayorpar=numpar1(lista)
        print (f'La lista 2 tiene mas pares que la lista 1: {mayorpar}')
    else: 
        mayorpar=numpar2(lista2)
        print (f'La lista 1 tiene mas pares que la lista 2: {mayorpar}')
    return mayorpar

def cantidadParesListas (lista,lista2):
    mayorimpar=0
    if numpar1(lista) < numpar2(lista2):
        mayorimpar=numpar1(lista)
        print (f'La lista 2 tiene mas pares que la lista 1: {mayorimpar}')
    else: 
        mayorimpar=numpar2(lista2)
        print (f'La lista 1 tiene mas pares que la lista 2: {mayorimpar}')
    return mayorimpar

def cantidadImparesListas (lista,lista2):
    mayorimpar=0
    if numimpar1(lista) < numimpar2(lista2):
        mayorimpar=numimpar1(lista)
        print (f'La lista 2 tiene mas impares que la lista 1: {mayorimpar}')
    else: 
        mayorimpar=numimpar2(lista2)
        print (f'La lista 1 tiene mas impares que la lista 2: {mayorimpar}')
    return mayorimpar

print("La suma de la lista 2 es:", sumaLista2(lista2))
print("El promedio de la lista 2 es:", promedioLista2 (lista2))
print ("El numero mayor de la lista 2 es:", mayorLista2 (lista2))
print ("El numero menor de la lista 2 es:", menorLista2 (lista2))
print()
sumaMayorListas(lista,lista2)
promedioConjunto(lista,lista2)

cantidadParesListas(lista,lista2)
cantidadImparesListas(lista,lista2)