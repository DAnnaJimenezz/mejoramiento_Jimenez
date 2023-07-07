from Cita import *
class Paciente (Cita):
    def __init__(self, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                  especialidadMedico, nombreConsultorio, nombreMedico, diasNoAgendados, horarioDisponible,
                  documento, tipoDocumento):
        super().__init__(nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                  especialidadMedico, nombreConsultorio, nombreMedico, diasNoAgendados, horarioDisponible)
        self.__documento = documento
        self.__tipoDocumento = tipoDocumento
        self.__registrarCita = []
    
    def registrarCita (self, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, 
                 diasNoAgendados, horarioDisponible):
        cit = Cita (nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, especialidadMedico, nombreConsultorio, nombreMedico, diasNoAgendados, horarioDisponible)
        self.__registrarCita.append(cit)

    def registroExitoso (self, registrarCita):
        self.__registrarCita.append(registrarCita)

    def eliminarCita ():
        pass

    def visualizarCitaHorarioDisponible ():
        pass

    def seleccionarEspecialidad ():
        pass

    def getDatos3 (self):
        return self.__nombrePaciente, self.__dia, self.__hora, self.__fechaAgenda, self.__motivoConsulta, self.__especialidadMedica, self.__nombreConsultorio, self.__nombreMedico, self.__diasNoAgendados, self.__horarioDisponible, self.__documento, self.__tipoDocumento