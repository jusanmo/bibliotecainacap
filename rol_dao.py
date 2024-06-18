from rol import Rol
from conection import Conexion
from beautifultable import BeautifulTable

class RolDao:
    def __init__(self)->None:
        self.__mysql= Conexion()
        
    @property
    def mysql(self):
        return self.__mysql
    
    
    #insertar rol
    def insertar(self,rol)->str:
        if self.buscarRol(rol.id_rol) is None:
            self.mysql.cursor.execute("INSERT INTO rol VALUES (%s,%s)",(rol.id_rol,rol.rol))
            self.mysql.conexion.commit()
            return 'ingresado correctamente'
        else:
            return 'no se pudo ingresar'
        
        
    #modificar rol
    def modificar(self,id_rol,nuevo_rol)->str:
        if self.buscarRol(id_rol) !=None:
            valores = (nuevo_rol)
            self.mysql.cursor.execute("UPDATE rol SET rol=%s WHERE id_rol=%s",valores)
            self.mysql.conexion.commit()
            return 'modificado correctamente'
        else:
            return 'no se pudo modificar'