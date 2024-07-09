from conection import Conexion
from categoria import Categoria

class CategoriaDao:
    def __init__(self):
        self.cnx = Conexion()

    def insertarCategoria(self, categoria: Categoria):
        try:
            self.cnx.conectar()
            query = "INSERT INTO categoria (id, genero, descripcion) VALUES (%s, %s, %s)"
            self.cnx.cursor.execute(query, (categoria.id, categoria.genero, categoria.descripcion))
            self.cnx.conexion.commit()
            return "Categoría agregada correctamente."
        except Exception as e:
            return f"Error al insertar categoría: {str(e)}"
        finally:
            self.cnx.cerrar()

    def listarCategorias(self):
        try:
            self.cnx.conectar()
            query = "SELECT id, genero, descripcion FROM categoria"
            self.cnx.cursor.execute(query)
            categorias = []
            for id, genero, descripcion in self.cnx.cursor.fetchall():
                categorias.append(Categoria(id, genero, descripcion))
            return categorias
        except Exception as e:
            print(f"Error al listar categorías: {str(e)}")
            return []
        finally:
            self.cnx.cerrar()

    def buscarCategoria(self, id_categoria):
        try:
            self.cnx.conectar()
            query = "SELECT id, genero, descripcion FROM categoria WHERE id = %s"
            self.cnx.cursor.execute(query, (id_categoria,))
            resultado = self.cnx.cursor.fetchone()
            if resultado:
                return Categoria(resultado[0], resultado[1], resultado[2])
            else:
                return None
        except Exception as e:
            print(f"Error al buscar categoría: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()

    def modificarCategoria(self, categoria: Categoria):
        try:
            self.cnx.conectar()
            query = "UPDATE categoria SET genero = %s, descripcion = %s WHERE id = %s"
            self.cnx.cursor.execute(query, (categoria.genero, categoria.descripcion, categoria.id))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Categoría modificada correctamente."
            else:
                return f"No se encontró ninguna categoría con ID {categoria.id}."
        except Exception as e:
            return f"Error al modificar categoría: {str(e)}"
        finally:
            self.cnx.cerrar()

    def eliminarCategoria(self, id_categoria):
        try:
            self.cnx.conectar()
            query = "DELETE FROM categoria WHERE id = %s"
            self.cnx.cursor.execute(query, (id_categoria,))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Categoría eliminada correctamente."
            else:
                return f"No se encontró ninguna categoría con ID {id_categoria}."
        except Exception as e:
            return f"Error al eliminar categoría: {str(e)}"
        finally:
            self.cnx.cerrar()
