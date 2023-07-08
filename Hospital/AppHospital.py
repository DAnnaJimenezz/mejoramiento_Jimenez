from Medico import *
from Paciente import *


while True:
    print('MENU PRINCIPAL')
    print('1- Paciente')
    print('2- Medico')
    print('3- Salir')
    opcion = int(input('Elija que funciones desea realizar:'))
    if opcion == 1:
        print ()
        print('MENU PACIENTE')
        print('1- Crear cita')
        print('2- Consultar cita')
        print('3- Eliminar cita')
        opcion = int(input('Elija que funciones desea realizar:'))
        if opcion==0:
            break
        elif opcion == 1:
            Paciente.CrearCita(Paciente.citas)
        elif opcion == 2:
            Paciente.consultarCita()
        elif opcion == 3:
            Paciente.eliminarCita()
        else:
            print('Ingrese una opcion valida')
    if opcion == 2:
        print ('MENU MEDICO')
        print('1- Consultar cita agendada')
        opcion = int(input('Elija que funciones desea realizar:'))
        if opcion ==0:
            break
        elif opcion == 1:
            Medico.buscarCita()
        else:
            print('Ingrese una opcion valida')