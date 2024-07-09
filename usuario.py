class Usuario:
    def __init__(self, rut, nombre, apellidos, correo, id_rol):
        self.__rut = rut
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.__id_rol = id_rol
    
    @property
    def rut(self):
        return self.__rut
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellidos(self):
        return self.__apellidos
    
    @property
    def correo(self):
        return self.__correo
    
    @property
    def id_rol(self):
        return self.__id_rol
