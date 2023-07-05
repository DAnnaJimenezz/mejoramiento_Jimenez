from Cita import *
class Medico (Cita):
    def __init__ (self, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, 
                 diasNoAgendados, horarioDisponible,
                 disponibilidad, consultorio):
        super().__init__(nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, 
                 diasNoAgendados, horarioDisponible)
        self.__disponibilidad = disponibilidad
        self.__consultorio = consultorio
        self.__citasAgendadas = []


    def citasAgendadas (self, nombrePaciente, dia, hora, fechaAgenda,):
        citaAgendada1 = ('Daniela Castro', 'Martes', '2:30pm', '12/08/2023')
        citaAgendada2 = ('Juan Guarnizo', 'Viernes', '6:00am', '27/07/2023')
        return nombrePaciente, dia, hora, fechaAgenda


    def getDatos4 (self):
        return self.__disponibilidad, self.__consultorio, self.__citasAgendadas 