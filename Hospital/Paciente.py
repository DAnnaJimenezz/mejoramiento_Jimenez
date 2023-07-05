from Cita import *
class Paciente (Cita):
    def __init__(self, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, 
                 diasNoAgendados, horarioDisponible, 
                 documento, tipoDocumento):
        super().__init__(nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, diasNoAgendados, horarioDisponible)
        self.__documento = documento
        self.__tipoDocumento = tipoDocumento
        self.__registrarCita = []

    def registrarCita (self, mesVigente, horarioDefinido, medicoSeleccionado, consultorioSeleccionado):
        citaRegistrada1 = ('Octubre', 'Mañana', 'Jaime Gonzales', 'Consultorio 67')
        citaRegistrada2 = ('Enero', 'Tarde', 'Sandra Jimenez', 'Consultorio 123')
        return mesVigente, horarioDefinido, medicoSeleccionado, consultorioSeleccionado
    
    def registroExitoso (self, registrarCita):
        self.__registrarCita.append(registrarCita)

    def eliminarCita ():
        pass

    def visualizarCitaHorarioDisponible ():
        pass

    def seleccionarEspecialidad ():
        pass

    def getDatos1 (self):
        return self.__documento, self.__tipoDocumento