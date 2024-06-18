from usuario import Usuario
from conection import Conexion
from beautifultable import BeautifulTable

class UsuarioDao:
    def __init__(self) -> None:
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql
    
    def insertarUsuario(self, usuario) -> str:
        if self.buscarUsuario(usuario.Rut) is None:
            self.mysql.cursor.execute("insert into Usuario values(%s,%s,%s,%s,%s)",(usuario.Rut, usuario.Nombre, usuario.Apellidos, usuario.Correo,))
            self.mysql.connection.commit()
            return 'Usuario ingresado correctamente'
        else:
            return 'El usuario ya existe'
        
    def buscarUsuario(self, codigo) -> str:
        valores = (codigo,)
        self.mysql.cursor.execute("SELECT * FROM Usuario WHERE codigo = %s", valores)
        resultado = self.mysql.cursor.fetchone()

        if resultado:
            return Usuario(*resultado)
        else:
            return None
        
    

