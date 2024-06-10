from prestamo import Prestamo
from conection import Conexion 
from beautifultable import BeautifulTable

class PrestamoDao:
    def __init__(self) -> None:
        self.__mysql = Conexion ()

    @property
    def mysql(self):
        return self.__mysql
    
def insertarPrestamo(self, prestamo):
    if self.mysqlbuscarPrestamo(Prestamo.Cod_Libros) is None:
        self.mysql.cursor.execute("INSERT INTO prestamo (%s)",(prestamo.Fecha,prestamo.Rut,prestamo.Cod_Libro))
        self.mysql.connection.commit()
        return 'Prestamo realizado con exito'
    else:
        return 'No se pudo realizar el prestamo ya que el libro ya esta prestado o retirado de la biblioteca'
    
    
        