#! /usr/bin/python3
import sys
from RepositorioConsultas import RepositorioConsultas
from Consulta import Consulta

from RepositorioCirugia import RepositorioCirugia
from Cirugia import Cirugia

class Menu:
    '''muestra el menu y lanza la función elegida'''

    def __init__(self):
        self.opciones = {
            "1": self.agregar_consulta,
            "2": self.agregar_cirugia,
            "3": self.modificar_consulta,
            "4": self.modificar_cirugia,
            "5": self.eliminar_consulta,
            "6": self.eliminar_cirugia,
            "7": self.listar_consulta,
            "8": self.listar_cirugia,
            "9": self.salir
        }
        self.repositorioConsultas = RepositorioConsultas()
        self.repositorioCirugias = RepositorioCirugia()

    def mostrar_menu(self):
        '''Muestra el menú de opciones'''
        print("""
Consultas y Cirugías:
-- Ingresos --
1. Ingresar consulta
2. Ingresar cirugía
-- Modificaciones --
3. Modificar consulta
4. Modificar cirugía
-- Eliminar --
5. Eliminar consulta
6. Eliminar cirugía
-- Listar --
7. Listar consulta
8. Listar cirugía
--
9. Salir
""")

    def ejecutar(self):
        '''muestra el menu y ejecuta la opción seleccionada'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
                input("Presione enter para continuar.")
            else:
                print("{0} no es una opción válida".format(opcion))

    def salir(self):
        print("Saliendo del programa")
        sys.exit(0)

    def agregar_consulta(self):
        nuevaConsulta = self.nuevaReserva("consulta")
        idConsultaAgregada = self.repositorioConsultas.store(nuevaConsulta)
        if idConsultaAgregada == 0:
            print ("Error al guardar la consulta nueva")
        else:
            print (f"Consulta nº{idConsultaAgregada} guardada con éxito")

    def agregar_cirugia(self):
        nuevaCirugia = self.nuevaReserva("cirugia")
        idCirugiaAgregada = self.repositorioCirugias.store(nuevaCirugia)
        if idCirugiaAgregada == 0:
            print ("Error al guardar la cirugia nueva")
        else:
            print (f"Cirugia nº{idCirugiaAgregada} guardada con éxito")

    def modificar_consulta(self):
        '''Solicita el id de una consulta.Busca la consulta  y actualiza su texto.modifica la fecha y hora de la consulta'''
        id = input("ingrese el id de la consulta a modificar: ")
        fecha = input("Ingrese la fecha correcta: ")
        hora = input("Ingrese la hora correcta: ")
        self.repositorioConsultas.update(id, fecha , hora)

    def modificar_cirugia(self):
        id = input("ingrese el id de la cirugia a modificar: ")
        fecha = input("Ingrese la fecha correcta: ")
        hora = input("Ingrese la hora correcta: ")
        self.repositorioCirugias.update(id, fecha, hora)

    def eliminar_consulta(self):
        id = input("Ingrese el id de consulta a borrar")
        if self.repositorioConsultas.delete(id):
            print("Consulta eliminada exitosamente")

    def eliminar_cirugia(self):
        id = input("Ingrese el id de la cirugia a borrar")
        if self.repositorioCirugias.delete(id):
            print("Cirugía eliminada exitosamente")

    def listar_consulta(self):
        consultas = self.repositorioConsultas.get_all()
        print("Listado de consultas:")
        for i in consultas:
             i.mostrarPorPantalla()

    def listar_cirugia(self):
        print("Listado de cirugias:")
        cirugia = self.repositorioCirugias.get_all()
        for i in cirugia:
            i.mostrarPorPantalla()

    def nuevaReserva(self, tipoDeReserva):
        hora = input("Ingrese la hora: ")
        fecha = input("Ingrese la fecha: ")
        nombrePaciente = input("Ingrese el nombre del paciente: ")
        diagnostico = input("Ingrese el diagnostico: ")
        if tipoDeReserva == "cirugia":
            numeroQuirofano = input("Ingrese el numero del quirofano donde será operado: ")
            horasAyuno = input("Ingrese las horas de ayuno necesarias antes de la cirugia: ")
            instrumentadorQuirurgico = input("Ingrese el nombre del instrumentador quirurgico: ")
            return Cirugia(fecha, hora, nombrePaciente, diagnostico, numeroQuirofano, horasAyuno, instrumentadorQuirurgico)
        if tipoDeReserva == "consulta":
            numeroConsultorio = input("Ingrese el numero de consultorio donde será atendido: ")
            return Consulta(fecha, hora, nombrePaciente, diagnostico, numeroConsultorio)

# Esta parte del código está fuera de la clase Menu.
# Si este archivo es el programa principal, entonces llamamos al método
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()

