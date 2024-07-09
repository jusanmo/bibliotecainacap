class Docente:

    def __init__(self,rut,nombre,apellidos)->None:
        self.__rut = rut
        self.__nombre = nombre
        self.__apellidos =apellidos
        
    @property
    def rut(self):
        return self.__rut
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellidos(self):
        return self.__apellidos