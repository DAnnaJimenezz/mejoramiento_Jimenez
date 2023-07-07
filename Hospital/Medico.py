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

    def getDatos2 (self):
        return self.__nombrePaciente, self.__dia, self.__hora, self.__fechaAgenda, self.__motivoConsulta, self.__especialidadMedica, self.__nombreConsultorio, self.__nombreMedico, self.__diasNoAgendados, self.__horarioDisponible, self.__disponibilidad, self.__consultorio