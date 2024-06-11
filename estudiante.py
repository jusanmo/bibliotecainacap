class Estudiante: 

    def __init__(self, Rut, Nombre, Apellido) -> None:
        self.Rut = Rut
        self.Nombre = Nombre
        self.Apellido = Apellido

    def Rut(self):
        return self.__Rut
    
    def Nombre(self):
        return self.__Nombre
    
    def Apellido(self):
        return self.__Apellido