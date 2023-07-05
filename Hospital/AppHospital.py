from Medico import *
from Paciente import *

# print (Medico.citasAgendadas)

# cita1 = Cita ('Si ahi disponibilidad', 'Consultorio 24', 'Juana Garcia', 'Martes', '9:00am', '13/09/2023', 
#               'Dolor frecuente de cabeza', 'Medicina interna', 'Consultorio Medicina General', 'Jorge Saldarriaga', 
#               'Fines de semana y Festivos', '24 Horas')
# print (cita1.citasAgendadas())

cita = Paciente.registrarCita()
cita.registroExitoso(cita)



paciente = Paciente.registrarCita()
paciente.registroExitoso(paciente)
print (paciente())