from bibliotecainacap.docente import Docente
from conection import Conexion
from beautifultable import Beautifultable
   
class EstudianteDao:
    def __init__(self) -> None:
        self.__mysql = Conexion ()
        
    @property
    def mysql(self):
        return self.__mysql

    #ingresar/insertar 
    def insertarEstudiante(self, estudiante)->str:
        if self.buscarEstudiante(estudiante.Rut) is None:  #revisar
            self.mysql.cursor.execute("insert into Docente values(%s,%s,%s)",(estudiante.Rut, estudiante.Nombre, estudiante.Apellidos))
            self.mysql.connection.commit() #revisar
            return 'Estudiante ingresado correctamente'
        else:
            return 'Estudiante ya no existe!'