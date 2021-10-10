#! /usr/bin/python3
from Repositorio import Repositorio
from Consulta import Consulta


class RepositorioConsultas(Repositorio):
    '''Ejecuta queries de la clase "Consultas" '''

    def get_one(self, id_consulta):
        '''Recibe un id (número entero). Retorna un objeto Consulta. Si no lo encuentra, retorna None.'''
        consulta = "SELECT fecha,hora,nombrePaciente,diagnostico,numeroConsultorio FROM consultas WHERE id = ?"
        result = self.cursor.execute(consulta, [id_consulta]).fetchone()

        if result == None:
            return None
        else:
            return Consulta(result[0], result[1], result[2], result[3], result[4])

    def get_all(self):
        print("TBD")

    def store(self, nota):
        print("TBD")

    def delete(self, nota):
        print("TBD")

    def update(self, nota):
        print("TBD")