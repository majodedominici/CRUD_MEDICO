#! /usr/bin/python3
from Repositorio import Repositorio
from Cirugia import Cirugia


class RepositorioCirugia(Repositorio):
    '''Ejecuta queries de la clase "Cirugia" '''

    def get_one(self, id_cirugia):
        '''Recibe un id (número entero). Retorna un objeto Cirugia. Si no lo encuentra, retorna None.'''
        cirugia = "SELECT id,fecha,hora,nombrePaciente,diagnostico, numeroQuirofano, horasAyuno, instrumentadorQuirurgico FROM cirugia WHERE id = ?"
        result = self.cursor.execute(cirugia, [id_cirugia]).fetchone()

        if result == None:
            return None
        else:
            return Cirugia(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7] )

    def get_all(self):
        '''Retorna todas las cirugias que haya almacenadas en la BD'''
        cirugia = "SELECT id,fecha,hora,nombrePaciente,diagnostico, numeroQuirofano, horasAyuno, instrumentadorQuirurgico FROM cirugia"
        result = self.cursor.execute(cirugia).fetchall()

        lista_de_cirugias = []

        for unResultado in result:
            cirugia = Cirugia(unResultado[1], unResultado[2], unResultado[3], unResultado[4], unResultado[5], unResultado[6], unResultado[7])
            cirugia.id = unResultado[0]
            lista_de_cirugias.append(cirugia)
        return lista_de_cirugias

    def store(self, cirugia):
        '''Recibe un objeto cirugia y lo almacena en la Base de Datos
                En caso de éxito, retorna el id de la cirugia, número generado por la base
                de datos. En caso de fracaso, retorna 0 '''
        try:
            query = "INSERT INTO cirugias ( fecha,hora,nombrePaciente,diagnostico,numeroQuirofano, horasAyuno, instrumentadorQuirurgico) VALUES (?, ? , ? , ? , ?, ?, ? )"
            result = self.cursor.execute(query, [cirugia.fecha, cirugia.hora, cirugia.nombrePaciente, cirugia.diagnostico, cirugia.numeroQuirofano, cirugia.horasAyuno, cirugia.instrumentadorQuirurgico])
            cirugia.id = result.lastrowid

            self.bd.commit()
            return cirugia.id
        except:
            self.bd.rollback()
            return 0

    def delete(self, id):
        '''Recibe un objeto Cirugia y lo elimina de la Base de Datos.
                Retorna True si tuvo éxito, False de lo contrario.'''
        try:
            query = "DELETE FROM cirugias WHERE id = ?"
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
        '''Recibe un objeto cirugia y actualiza sus datos en la base de datos, dependiendo el id que ingrese el usuario'''
        try:
            query = "UPDATE cirugias SET fecha = ?, hora = ? WHERE id = ?"
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