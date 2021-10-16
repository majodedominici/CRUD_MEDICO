from Reserva import Reserva


class Cirugia(Reserva):
    def __init__(self, fecha, hora, nombrePaciente, diagnostico, numeroQuirofano, horasAyuno, instrumentadorQuirurgico):
        Reserva.__init__(self, fecha, hora, nombrePaciente, diagnostico)
        self.numeroQuirofano = numeroQuirofano
        self.horasAyuno = horasAyuno
        self.instrumentadorQuirurgico = instrumentadorQuirurgico

    def mostrarPorPantalla(self):
        print(f"Id: {self.id}"
              f"\nFecha: {self.fecha}"
              f"\nHora: {self.hora}"
              f"\nDiagnostico: {self.diagnostico}"
              f"\nPaciente: {self.nombrePaciente}"
              f"\nNumero de Quirofano: {self.numeroQuirofano}"
              f"\nHora de Ayuno: {self.horasAyuno}"
              f"\nInstrumentador Quirurgico: {self.instrumentadorQuirurgico}"
              f"\n--")