from conection import Conexion
from multa import Multa

class MultaDao:
    def __init__(self):
        self.cnx = Conexion()

    def registrar_multa(self, multa):
        try:
            self.cnx.conectar()
            query = "INSERT INTO multas (Rut_usuario, Cod_libro, Dias_retraso, Monto, Pagada) VALUES (%s, %s, %s, %s, %s)"
            self.cnx.cursor.execute(query, (multa.rut_usuario, multa.cod_libro, multa.dias_retraso, multa.monto, multa.pagada))
            self.cnx.conexion.commit()
            return "Multa registrada correctamente."
        except Exception as e:
            return f"Error al registrar multa: {str(e)}"
        finally:
            self.cnx.cerrar()

    def marcar_multa_pagada(self, id_multa):
        try:
            self.cnx.conectar()
            query = "UPDATE multas SET Pagada = 1 WHERE ID = %s"
            self.cnx.cursor.execute(query, (id_multa,))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Multa marcada como pagada correctamente."
            else:
                return f"No se encontró ninguna multa con ID {id_multa}."
        except Exception as e:
            return f"Error al marcar multa como pagada: {str(e)}"
        finally:
            self.cnx.cerrar()

    def listar_multas(self):
        try:
            self.cnx.conectar()
            query = "SELECT ID, Rut_usuario, Cod_libro, Dias_retraso, Monto, Pagada FROM multas"
            self.cnx.cursor.execute(query)
            multas = []
            for id_multa, rut_usuario, cod_libro, dias_retraso, monto, pagada in self.cnx.cursor.fetchall():
                multas.append(Multa(id_multa, rut_usuario, cod_libro, dias_retraso, monto, pagada))
            return multas
        except Exception as e:
            print(f"Error al listar multas: {str(e)}")
            return []
        finally:
            self.cnx.cerrar()

    def buscar_multa_por_id(self, id_multa):
        try:
            self.cnx.conectar()
            query = "SELECT ID, Rut_usuario, Cod_libro, Dias_retraso, Monto, Pagada FROM multas WHERE ID = %s"
            self.cnx.cursor.execute(query, (id_multa,))
            resultado = self.cnx.cursor.fetchone()
            if resultado:
                id_multa, rut_usuario, cod_libro, dias_retraso, monto, pagada = resultado
                return Multa(id_multa, rut_usuario, cod_libro, dias_retraso, monto, pagada)
            else:
                return None
        except Exception as e:
            print(f"Error al buscar multa por ID: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()