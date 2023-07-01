#Diseñar e implementar un programa que solicite a su usuario un valor no negativo n y visualice la siguiente salida:

def valorNoNegativo ():
    n = int(input("Escriba un numero positivo: "))
    for i in range(n, 0, -1):
        for h in range(1, i+1, +1):
            print(h, end="")
        print()

valorNoNegativo ()