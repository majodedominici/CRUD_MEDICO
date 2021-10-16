from Reserva import Reserva

class Consulta(Reserva):
    def __init__(self,fecha,hora,nombrePaciente,diagnostico,numeroConsultorio):
        Reserva.__init__(self,fecha,hora,nombrePaciente,diagnostico)
        self.numeroConsultorio = numeroConsultorio

    def mostrarPorPantalla(self):
        print(f"Id: {self.id}"
              f"\nFecha: {self.fecha}"
              f"\nHora: {self.hora}"
              f"\nConsultorio: {self.numeroConsultorio}"
              f"\nDiagnostico: {self.diagnostico}"
              f"\nPaciente: {self.nombrePaciente}"
              f"\n--")
