#! /usr/bin/python3
import sys
from RepositorioConsultas import RepositorioConsultas
from Consulta import Consulta

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
            else:
                print("{0} no es una opción válida".format(opcion))

    def salir(self):
        print("Saliendo del programa")
        sys.exit(0)

    def agregar_consulta(self):
        hora= input("Ingrese la hora: ")
        fecha = input("Ingrese la fecha: ")
        nombrePaciente = input("Ingrese el nombre del paciente: ")
        diagnostico = input("Ingrese el diagnostico: ")
        numeroConsultorio = input("Ingrese el numero de consultorio donde será atendido: ")
        nuevaConsulta = Consulta(fecha,hora,nombrePaciente,diagnostico,numeroConsultorio)
        self.repositorioConsultas.store(nuevaConsulta)

    def agregar_cirugia(self):
        print("TBD")

    def modificar_consulta(self):
        '''Solicita el id de una consulta.Busca la consulta  y actualiza su texto.modifica la fecha y hora de la consulta'''
        id = input("ingrese el id de la consulta a modificar: ")
        fecha = input("Ingrese la fecha correcta: ")
        hora = input("Ingrese la hora correcta: ")


        self.repositorioConsultas.update(id, fecha , hora)

    def modificar_cirugia(self):
        print("TBD")


    def eliminar_consulta(self):
        id = input("Ingrese el id de consulta a borrar")
        self.repositorioConsultas.delete(id)

    def eliminar_cirugia(self):
        print("TBD")

    def listar_consulta(self):
        consultas = self.repositorioConsultas.get_all()
        for i in consultas:
             print(i.id, i.fecha, i.hora, i.numeroConsultorio, i.diagnostico, i.nombrePaciente)


    def listar_cirugia(self):
        print("TBD")



# Esta parte del código está fuera de la clase Menu.
# Si este archivo es el programa principal, entonces llamamos al método
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()

