from Reserva import Reserva

class Consulta(Reserva):
    def __init__(self,fecha,hora,nombrePaciente,diagnostico,numeroConsultorio):
        Reserva.__init__(self,fecha,hora,nombrePaciente,diagnostico)
        self.numeroConsultorio = numeroConsultorio
