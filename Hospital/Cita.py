class Cita ():
    def __init__(self, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, 
                 diasNoAgendados, horarioDisponible):
        self.__nombrePaciente = nombrePaciente
        self.__dia = dia
        self.__hora = hora 
        self.__fechaAgenda = fechaAgenda
        self.__motivoConsulta = motivoConsulta
        self.__especialidadMedica = especialidadMedico
        self.__nombreConsultorio = nombreConsultorio
        self.__nombreMedico = nombreMedico
        self.__diasNoAgendados = diasNoAgendados
        self.__horarioDisponible = horarioDisponible
    
    def getDatos1 (self):
        return self.__nombrePaciente, self.__dia, self.__hora, self.__hora, self.__fechaAgenda, self.__motivoConsulta, self.__especialidadMedica, self.__nombreConsultorio, self.__nombreMedico, self.__diasNoAgendados, self.__horarioDisponible