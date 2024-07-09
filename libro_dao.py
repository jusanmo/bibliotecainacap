from conection import Conexion
from libro import Libro

class LibroDao:
    def __init__(self):
        self.cnx = Conexion()

    def insertar_libro(self, libro: Libro):
        try:
            self.cnx.conectar()
            query = "INSERT INTO libro (cod_libro, titulo, descripcion, id_categoria, cantidad) VALUES (%s, %s, %s, %s, %s)"
            self.cnx.cursor.execute(query, (libro.cod_libro, libro.titulo, libro.descripcion, libro.id_categoria, libro.cantidad))
            self.cnx.conexion.commit()
            return "Libro agregado correctamente."
        except Exception as e:
            return f"Error al insertar libro: {str(e)}"
        finally:
            self.cnx.cerrar()

    def buscar_libro_por_codigo(self, cod_libro):
        try:
            self.cnx.conectar()
            query = "SELECT cod_libro, titulo, descripcion, id_categoria, cantidad FROM libro WHERE cod_libro = %s"
            self.cnx.cursor.execute(query, (cod_libro,))
            resultado = self.cnx.cursor.fetchone()
            if resultado:
                return Libro(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            else:
                return None
        except Exception as e:
            print(f"Error al buscar libro por código: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()

    def listar_libros(self):
        try:
            self.cnx.conectar()
            query = "SELECT cod_libro, titulo, descripcion, id_categoria, cantidad FROM libro"
            self.cnx.cursor.execute(query)
            libros = []
            for cod_libro, titulo, descripcion, id_categoria, cantidad in self.cnx.cursor.fetchall():
                libros.append(Libro(cod_libro, titulo, descripcion, id_categoria, cantidad))
            return libros
        except Exception as e:
            print(f"Error al listar libros: {str(e)}")
            return []
        finally:
            self.cnx.cerrar()

    def modificar_libro(self, libro: Libro):
        try:
            self.cnx.conectar()
            query = "UPDATE libro SET titulo = %s, descripcion = %s, id_categoria = %s, cantidad = %s WHERE cod_libro = %s"
            self.cnx.cursor.execute(query, (libro.titulo, libro.descripcion, libro.id_categoria, libro.cantidad, libro.cod_libro))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Libro modificado correctamente."
            else:
                return f"No se encontró ningún libro con código {libro.cod_libro}."
        except Exception as e:
            return f"Error al modificar libro: {str(e)}"
        finally:
            self.cnx.cerrar()

    def eliminar_libro(self, cod_libro):
        try:
            self.cnx.conectar()
            query = "DELETE FROM libro WHERE cod_libro = %s"
            self.cnx.cursor.execute(query, (cod_libro,))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Libro eliminado correctamente."
            else:
                return f"No se encontró ningún libro con código {cod_libro}."
        except Exception as e:
            return f"Error al eliminar libro: {str(e)}"
        finally:
            self.cnx.cerrar()

    def actualizar_cantidad(self, codigo_libro, nueva_cantidad):
        try:
            self.cnx.conectar()
            query = "UPDATE libro SET cantidad = %s WHERE cod_libro = %s"
            self.cnx.cursor.execute(query, (nueva_cantidad, codigo_libro))
            self.cnx.conexion.commit()
            return "Cantidad actualizada correctamente."
        except Exception as e:
            return f"Error al actualizar cantidad de libros: {str(e)}"
        finally:
            self.cnx.cerrar()

    def buscarLibro(self, cod_libro):
        try:
            self.cnx.conectar()
            query = "SELECT cod_libro, titulo, descripcion, id_categoria, cantidad FROM libro WHERE cod_libro = %s"
            self.cnx.cursor.execute(query, (cod_libro,))
            result = self.cnx.cursor.fetchone()
            if result:
                return Libro(result[0], result[1], result[2], result[3], result[4])
            else:
                return None
        except Exception as e:
            print(f"Error al buscar libro: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()