class Prestamo:

    def __init__(self, Fecha, Rut, Cod_Libro) -> None:
        self.Fecha = Fecha
        self.Rut = Rut
        self.Cod_Libro = Cod_Libro

    def Fecha(self):
        return self.__Fecha
    
    def Rut(self):
        return self.__Rut
    
    def Cod_Libro(self):
        return self.__Cod_Libro
