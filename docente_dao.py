from bibliotecainacap.docente import Docente
from conection import Conexion
from beautifultable import Beautifultable
   
class DocenteDao:
    def __init__(self) -> None:
        self.__mysql = Conexion ()
        
    @property
    def mysql(self):
        return self.__mysql

    #ingresar/insertar 
    def insertarDocente(self, docente)->str:
        if self.buscarDocente(docente.rut) is None:  #revisar
            self.mysql.cursor.execute("insert into Docente values(%s,%s,%s)",(docente.rut, docente.nombre, docente.apellidos))
            self.mysql.connection.commit() #revisar
            return 'Docente ingresado correctamente'
        else:
            return 'Docente ya no existe!'
        