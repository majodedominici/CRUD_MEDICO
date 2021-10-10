#! /usr/bin/python3
import sys

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
        print("TBD")

    def agregar_cirugia(self):
        print("TBD")

    def modificar_consulta(self):
        print("TBD")

    def modificar_cirugia(self):
        print("TBD")


    def eliminar_consulta(self):
        print("TBD")

    def eliminar_cirugia(self):
        print("TBD")

    def listar_consulta(self):
        print("TBD")

    def listar_cirugia(self):
        print("TBD")
# Esta parte del código está fuera de la clase Menu.
# Si este archivo es el programa principal, entonces llamamos al método
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()

