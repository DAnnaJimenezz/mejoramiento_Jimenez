# Calcular el máximo de números positivos introducidos por
# teclado, sabiendo que metemos números hasta que
# introduzcamos uno negativo. El negativo no cuenta.

def maximoPositivo ():
    cont=0 
    num=1
    while num>=0:
        num=int(input("Escriba un numero positivo: "))
        if num>=0:
            cont+=1
        else: 
            print(f"Usted ingreso {cont} numeros positivos") 

maximoPositivo ()