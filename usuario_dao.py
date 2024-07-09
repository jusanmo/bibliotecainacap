from conection import Conexion
from usuario import Usuario

class UsuarioDao:
    def __init__(self):
        self.cnx = Conexion()
        self.mysql = Conexion()

    def insertarUsuario(self, usuario):
        try:
            self.mysql.conectar()
            query = "INSERT INTO usuario (Rut, Nombre, Apellidos, Correo, ID_ROL) VALUES (%s, %s, %s, %s, %s)"
            values = (usuario.rut, usuario.nombre, usuario.apellidos, usuario.correo, usuario.id_rol)
            self.mysql.cursor.execute(query, values)
            self.mysql.conexion.commit()
            return 'Usuario ingresado correctamente'
        except Exception as e:
            return f'Error al insertar usuario: {str(e)}'
        finally:
            self.mysql.cerrar()

    def listarUsuarios(self):
        try:
            self.mysql.conectar()
            query = "SELECT * FROM usuario"
            self.mysql.cursor.execute(query)
            result = self.mysql.cursor.fetchall()
            usuarios = []
            for row in result:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4])
                usuarios.append(usuario)
            return usuarios
        except Exception as e:
            print(f"Error al listar usuarios: {str(e)}")
            return []
        finally:
            self.mysql.cerrar()

    def eliminarUsuario(self, rut):
        try:
            if not self.existeUsuario(rut):
                return 'No hay usuarios para eliminar'
            
            self.mysql.conectar()
            query = "DELETE FROM usuario WHERE Rut = %s"
            self.mysql.cursor.execute(query, (rut,))
            if self.mysql.cursor.rowcount > 0:
                self.mysql.conexion.commit()
                return 'Usuario eliminado correctamente'
            else:
                return 'No se encontró ningún usuario con ese Rut'
        except Exception as e:
            return f'Error al eliminar usuario: {str(e)}'
        finally:
            self.mysql.cerrar()

    def buscarUsuario(self, rut):
        try:
            self.mysql.conectar()
            query = "SELECT * FROM usuario WHERE Rut = %s"
            self.mysql.cursor.execute(query, (rut,))
            result = self.mysql.cursor.fetchone()
            if result:
                return Usuario(result[0], result[1], result[2], result[3], result[4])
            else:
                return None
        except Exception as e:
            print(f"Error al buscar usuario: {str(e)}")
            return None
        finally:
            self.mysql.cerrar()

    def existeUsuario(self, rut):
        try:
            self.mysql.conectar()
            query = "SELECT * FROM usuario WHERE Rut = %s"
            self.mysql.cursor.execute(query, (rut,))
            result = self.mysql.cursor.fetchone()
            return result is not None
        except Exception as e:
            print(f"Error al verificar existencia de usuario: {str(e)}")
            return False
        finally:
            self.mysql.cerrar()

    def modificarUsuario(self, usuario: Usuario):
        try:
            self.cnx.conectar()
            query = "UPDATE usuario SET nombre = %s, apellidos = %s, correo = %s, id_rol = %s WHERE rut = %s"
            self.cnx.cursor.execute(query, (usuario.nombre, usuario.apellidos, usuario.correo, usuario.id_rol, usuario.rut))
            self.cnx.conexion.commit()
            if self.cnx.cursor.rowcount > 0:
                return "Usuario modificado correctamente."
            else:
                return f"No se encontró ningún usuario con Rut {usuario.rut}."
        except Exception as e:
            return f"Error al modificar usuario: {str(e)}"
        finally:
            self.cnx.cerrar()

    def buscar_usuario_por_rut(self, rut):
        try:
            self.cnx.conectar()
            query = "SELECT rut, nombre, apellidos, correo, id_rol FROM usuario WHERE rut = %s"
            self.cnx.cursor.execute(query, (rut,))
            usuario_data = self.cnx.cursor.fetchone()
            if usuario_data:
                rut, nombre, apellidos, correo, id_rol = usuario_data
                return Usuario(rut, nombre, apellidos, correo, id_rol)
            else:
                return None
        except Exception as e:
            print(f"Error al buscar usuario por rut: {str(e)}")
            return None
        finally:
            self.cnx.cerrar()