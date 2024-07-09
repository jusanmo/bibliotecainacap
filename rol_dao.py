from conection import Conexion
from rol import Rol

class RolDao:
    def __init__(self):
        self.mysql = Conexion()

    def listarRoles(self):
        try:
            self.mysql.conectar()
            cursor = self.mysql.cursor
            cursor.execute("SELECT * FROM roles")
            roles = []
            for id, nombre in cursor.fetchall():
                roles.append(Rol(id, nombre))
            return roles
        except Exception as e:
            print(f"Error al listar roles: {e}")
            return None
        finally:
            self.mysql.cerrar()