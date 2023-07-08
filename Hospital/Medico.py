from Paciente import *
class Medico (Paciente):
    especializaciones = []
    Esp = {}
    def __init__ (self, documento, tipoDocumento, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                 especialidadMedico, nombreConsultorio, nombreMedico, 
                 diasNoAgendados, horarioDisponible,
                 disponibilidad, consultorio):
        super().__init__(documento, tipoDocumento)
        self.__disponibilidad = disponibilidad
        self.__consultorio = consultorio
        Medico.especializaciones = []
        Medico.Esp = {}
        

    def buscarCita():
        for Paciente.Cit in Paciente.citas:
            nombreBusqueda = input('Ingrese el nombre del paciente que tiene la cita: ')
            if Paciente.Cit["NombrePaciente"] == nombreBusqueda:
                print("Cita encontrada:")
                print("NombrePaciente: ", Paciente.Cit["NombrePaciente"])
                print("Dias: ", Paciente.Cit["Dias"])
                print("Horas: ", Paciente.Cit["Horas"])
                print("Fechas: ", Paciente.Cit["Fechas"])
                print("Motivo: ", Paciente.Cit["Motivo"])
                print("DiasNoAgendados", Paciente.Cit["DiaNoAgendados"])
            else:
                print("Cita no encontrada.")

    def getDatos2 (self):
        return f'{self.__disponibilidad},{self.__consultorio}'