from datetime import datetime
from conection import Conexion
from usuario import Usuario
from libro import Libro
from prestamo import Prestamo



class PrestamoDao:
    def __init__(self):
        self.cnx = Conexion()

    def realizarPrestamo(self, prestamo: Prestamo):
        try:
            self.cnx.conectar()
            # Insertar el préstamo
            query_prestamo = "INSERT INTO prestamos (rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)"
            self.cnx.cursor.execute(query_prestamo, (prestamo.rut_usuario, prestamo.cod_libro, prestamo.fecha_prestamo, prestamo.fecha_devolucion))
            
            # Actualizar la cantidad del libro
            query_update = "UPDATE libro SET cantidad = cantidad - 1 WHERE cod_libro = %s"
            self.cnx.cursor.execute(query_update, (prestamo.cod_libro,))
            
            self.cnx.conexion.commit()
            return "Préstamo realizado y cantidad de libro actualizada correctamente."
        except Exception as e:
            return f"Error al realizar el préstamo: {str(e)}"
        finally:
            self.cnx.cerrar()

    def buscarPrestamoPorId(self, id_prestamo):
        try:
            self.cnx.conectar()
            query = "SELECT id, rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion, renovaciones FROM prestamos WHERE id = %s"
            self.cnx.cursor.execute(query, (id_prestamo,))
            resultado = self.cnx.cursor.fetchone()
            if resultado:
                return Prestamo(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            else:
                return None
        except Exception as e:
            print(f"Error al buscar préstamo por ID: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()
            
    def listarPrestamos(self):
        try:
            self.cnx.conectar()
            query = """
                SELECT p.id, p.rut_usuario, p.cod_libro, p.fecha_prestamo, p.fecha_devolucion,
                       u.nombre as nombre_usuario, u.apellidos as apellidos_usuario, u.rut as rut_usuario,
                       l.titulo as titulo_libro
                FROM prestamos p
                INNER JOIN usuario u ON p.rut_usuario = u.rut
                INNER JOIN libro l ON p.cod_libro = l.cod_libro
            """
            self.cnx.cursor.execute(query)
            prestamos = []
            for row in self.cnx.cursor.fetchall():
                prestamo = {
                    'id': row[0],
                    'usuario': {
                        'nombre': row[5],
                        'apellidos': row[6],
                        'rut': row[7]
                    },
                    'libro': {
                        'titulo': row[8]
                    },
                    'fecha_prestamo': row[3],
                    'fecha_devolucion': row[4]
                }
                prestamos.append(prestamo)
            return prestamos
        except Exception as e:
            print(f"Error al listar préstamos: {str(e)}")
            return []
        finally:
            self.cnx.cerrar()
    def actualizarPrestamo(self, prestamo: Prestamo):
        try:
            self.cnx.conectar()
            query = "UPDATE prestamos SET fecha_devolucion = %s, renovaciones = %s WHERE id = %s"
            self.cnx.cursor.execute(query, (prestamo.fecha_devolucion, prestamo.renovaciones, prestamo.id))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Préstamo actualizado correctamente."
            else:
                return f"No se encontró ningún préstamo con ID {prestamo.id}."
        except Exception as e:
            return f"Error al actualizar préstamo: {str(e)}"
        finally:
            self.cnx.cerrar()

    def eliminarPrestamo(self, id_prestamo):
        try:
            self.cnx.conectar()
            query = "DELETE FROM prestamos WHERE id = %s"
            self.cnx.cursor.execute(query, (id_prestamo,))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Préstamo eliminado correctamente."
            else:
                return f"No se encontró ningún préstamo con ID {id_prestamo}."
        except Exception as e:
            return f"Error al eliminar préstamo: {str(e)}"
        finally:
            self.cnx.cerrar()

    def buscarPrestamo(self, id_prestamo):
        try:
            self.cnx.conectar()
            query = "SELECT id, rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion FROM prestamos WHERE id = %s"
            self.cnx.cursor.execute(query, (id_prestamo,))
            resultado = self.cnx.cursor.fetchone()
            if resultado:
                return Prestamo(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            else:
                return None
        except Exception as e:
            print(f"Error al buscar préstamo por ID: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()

    def renovarPrestamo(self, prestamo: Prestamo):
        try:
            self.cnx.conectar()
            query = "UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s"
            self.cnx.cursor.execute(query, (prestamo.fecha_devolucion, prestamo.id))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Préstamo renovado correctamente."
            else:
                return f"No se encontró ningún préstamo con ID {prestamo.id}."
        except Exception as e:
            return f"Error al renovar préstamo: {str(e)}"
        finally:
            self.cnx.cerrar()

    def devolverLibro(self, id_prestamo):
        try:
            self.cnx.conectar()
            query = "DELETE FROM prestamos WHERE id = %s"
            self.cnx.cursor.execute(query, (id_prestamo,))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Préstamo devuelto correctamente."
            else:
                return f"No se encontró ningún préstamo con ID {id_prestamo}."
        except Exception as e:
            return f"Error al devolver préstamo: {str(e)}"
        finally:
            self.cnx.cerrar()

    def listar_prestamos_activos(self):
        try:
            self.cnx.conectar()
            hoy = datetime.now().date()
            query = "SELECT id, rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion FROM prestamos WHERE fecha_devolucion >= %s"
            self.cnx.cursor.execute(query, (hoy,))
            prestamos = []
            for id, rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion in self.cnx.cursor.fetchall():
                prestamos.append(Prestamo(id, rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion))
            return prestamos
        except Exception as e:
            print(f"Error al listar préstamos activos: {str(e)}")
            return []
        finally:
            self.cnx.cerrar()