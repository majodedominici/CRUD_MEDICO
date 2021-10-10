from Reserva import Reserva


class Cirugia(Reserva):
    def __init__(self, fecha, hora, nombrePaciente, diagnostico, numeroQuirofano, horasAyuno, instrumentadorQuirurgico):
        Reserva.__init__(self, fecha, hora, nombrePaciente, diagnostico, numeroQuirofano, horasAyuno, instrumentadorQuirurgico)
        self.numeroQuirofano = numeroQuirofano
        self.horasAyuno = horasAyuno
        self.instrumentadorQuirurgico = instrumentadorQuirurgico
