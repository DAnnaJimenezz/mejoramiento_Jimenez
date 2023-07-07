from Medico import *
from Paciente import *

cita1 = Paciente ('Juana Baron', 'Jueves', '3:30pm', '13/02/24', 
                  'Tengo fuerte dolor de estomago', 'Medicina General', 
                  'Consultorio Medicina Genreal','Pedro Gomez', 'Domingos y dias festivos', 
                  '24 horas del dia', '234567', 'C.C')
citaAgendada1 = Medico ('David Lopez', 'Lunes','09:00am', '31/04/25', 'Cirugia', 
                        'Cirujano', 'Consultorio de Cirugia', 'Diana Bedolla','Domingos y festivos', 
                        'Desde las 6:00am hasta las 12:00pm', 'Solo el lunes', 'Consultorio 145')
while True:
    opcion = int(input('Elija que funciones desea realizar:'))
    print()
    if opcion == 0:
        break 
    elif opcion == 1:
        print ('CITA AGENDADA PARA LA PACIENTE JUANA BARON')
        print (cita1.getDatos3())
    elif opcion == 2:
        print ('CITA 1 AGENDADA MEDICA DIANA BEDOLLA')
        print (citaAgendada1.getDatos2())
    else:
        print('Ingrese una opcion valida')