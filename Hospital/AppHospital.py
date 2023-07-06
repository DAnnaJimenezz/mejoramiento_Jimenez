from Medico import *
from Paciente import *

print ('CITA 1 AGENDADA MEDICA DIANA BEDOLLA')
citaAgendada1 = Medico ('Jose Hernandez', 'Lunes', '09:00am', '31/04/25', 'Cirugia', 'Cirujano', 'Consultorio de Cirugia', 'Diana Bedolla', 'Domingos y festivos', 'Desde las 6:00am hasta las 12:00pm', 'Solo el lunes', 'Consultorio 145')
print (citaAgendada1.getDatos4())
print ()
print ('CITA 1 AGENDADA MEDICO JESUS CARVAJAL')
citaAgendada2 = Medico ('Josue Piñeros', 'Miercoles', '1:00pm', '27/07/22', 'Dolor de muela frecuente', 'Odontologo', 'Consultorio de Odontologia', 'Jesus Carvajal', 'Domingos y festivos', 'Desde la 1:00pm hasta las 6:00pm', 'Miercoles solamente', 'Consultorio 1')
print (citaAgendada2.getDatos4())
print ()
cita1 = Cita ('Juana Baron', 'Jueves', '3:30pm', '13/02/24', 'Tengo fuerte dolor de estomago', 'Medicina General', 'Consultorio Medicina Genreal', 'Pedro Gomez', 'Domingos y dias festivos', '24 horas del dia')
print (cita1.getDatos2())