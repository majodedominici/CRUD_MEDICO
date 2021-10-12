#! /usr/bin/python3
from Repositorio import Repositorio
from Consulta import Consulta


class RepositorioConsultas(Repositorio):
    '''Ejecuta queries de la clase "Consultas" '''

    def get_one(self, id_consulta):
        '''Recibe un id (número entero). Retorna un objeto Consulta. Si no lo encuentra, retorna None.'''
        consulta = "SELECT id,fecha,hora,nombrePaciente,diagnostico,numeroConsultorio FROM consultas WHERE id = ?"
        result = self.cursor.execute(consulta, [id_consulta]).fetchone()

        if result == None:
            return None
        else:
            return Consulta(result[0], result[1], result[2], result[3], result[4], result[5])

    def get_all(self):
        '''Retorna todas las consultas que haya almacenadas en la BD'''
        consulta = "SELECT id, fecha,hora,nombrePaciente,diagnostico,numeroConsultorio FROM consultas"
        result = self.cursor.execute(consulta).fetchall()

        lista_de_consultas = []

        for unResultado in result:
            consulta = Consulta(unResultado[1], unResultado[2], unResultado[3], unResultado[4], unResultado[5])
            consulta.id = unResultado[0]
            lista_de_consultas.append(consulta)
        return lista_de_consultas

    def store(self, consulta):
        '''Recibe un objeto consulta y lo almacena en la Base de Datos
                En caso de éxito, retorna el id de la consulta, número generado por la base
                de datos. En caso de fracaso, retorna 0 '''
        try:
            query = "INSERT INTO consultas ( fecha,hora,nombrePaciente,diagnostico,numeroConsultorio) VALUES (?, ? , ? , ? , ? )"
            result = self.cursor.execute(query, [consulta.fecha, consulta.hora, consulta.nombrePaciente, consulta.diagnostico, consulta.numeroConsultorio])
            consulta.id = result.lastrowid

            self.bd.commit()
            return consulta.id
        except:
            self.bd.rollback()
            return 0

    def delete(self, id):
        '''Recibe un objeto Consulta y lo elimina de la Base de Datos.
                Retorna True si tuvo éxito, False de lo contrario.'''
        try:
            query = "DELETE FROM consultas WHERE id = ?"
            self.cursor.execute(query, [id])
            c = self.cursor.rowcount
            if c == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False

    def update(self, id, fecha, hora):
        '''Recibe un objeto consulta y actualiza sus datos en la base de datos, dependiendo el id que ingrese el usuario'''
        try:
            query = "UPDATE consultas SET fecha = ?, hora = ? WHERE id = ?"
            result = self.cursor.execute(query, [fecha, hora, id])
            if result.rowcount == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False