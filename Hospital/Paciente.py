from Cita import *
class Paciente (Cita):
    citas=[]
    Cit={}
    def __init__(self, nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                  especialidadMedico, nombreConsultorio, nombreMedico, diasNoAgendados, horarioDisponible, documento, tipoDocumento):
        super().__init__(nombrePaciente, dia, hora, fechaAgenda, motivoConsulta, 
                  especialidadMedico, nombreConsultorio, nombreMedico, diasNoAgendados, horarioDisponible)
        self.__documento = documento
        self.__tipoDocumento = tipoDocumento
        Paciente.citas=[]
        Paciente.Cit={}
    

    def CrearCita(citas):
        nombrePaciente= input("Ingrese el nombre del paciente: ")
        dia =input("Ingrese el dia de la cita:")
        hora = int(input("Ingrese la hora de la cita:"))
        fechaAgendada= int(input("Ingrese la fecha agendada:"))
        motivoConsulta= input("Ingrese el motivo de la cita:")
        especialidadMedico = input("Ingrese la especialidad del medico:")
        nombreConsultorio= input("Ingrese el nombre del consultorio:")
        nombreMedico= input("Ingrese el nombre del medico:")
        diasNoAgendados=input('Ingrese los dias no registrados:')
        horarioDisponible=int(input('Ingrese la hora disponible:'))
        documento=int(input('Ingrese su numero de documento:'))
        tipoDocuemnto=input('Ingrese el tipo de documento:')
        
        Paciente.Cit= {
        "NombrePaciente":nombrePaciente,
        "Dias":dia,
        "Horas":hora,
        "Fechas":fechaAgendada,
        "Motivo":motivoConsulta,
        "Especialidad":especialidadMedico,
        "NombreConsultorio":nombreConsultorio,
        "NombreMedico":nombreMedico,
        "DiaNoAgendados":diasNoAgendados,
        "Horario":horarioDisponible,
        "NumeroDocumento":documento,
        "TipoDocumento":tipoDocuemnto
        }
        Paciente.citas.append(Paciente.Cit)
        print("CITA ALMACENADA CORRECTAMENTE.")

    def eliminarCita ():
        for Paciente.Cit in Paciente.citas:
            eliminarCita = input('Ingrese el nombre guardado de la cita para eliminar:')
            if Paciente.Cit["NombrePaciente"] == eliminarCita:
                Paciente.citas.remove(Paciente.Cit)
                print ("CITA ELIMINADA CORRECTAMENTE.")

    def consultarCita ():
        for Paciente.Cit in Paciente.citas:
            nombreBusqueda = input('Ingrese su nombre para buscar las citas registradas:')
            if Paciente.Cit["NombrePaciente"] == nombreBusqueda:
                print("Cita encontrada:")
                print("NombreMedico: ", Paciente.Cit["NombreMedico"])
                print("NombreConsultorio: ", Paciente.Cit["NombreConsultorio"])
                print("Dias: ", Paciente.Cit["Dias"])
                print("Horas: ", Paciente.Cit["Horas"])
            else:
                print ("NO SE ENCUENTRA NINGUNA CITA.")

    def getDatos3 (self):
        return f'{self.__documento},{self.__tipoDocumento}'