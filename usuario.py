class Usuario:

    def __init__(self, Rut, Nombre, Apellidos, Correo):
        self.__Rut = Rut
        self.__Nombre = Nombre
        self.__Apellidos = Apellidos
        self.__Correo = Correo
       

        @property
        def Rut(self):
            return self.__Rut
        
        @property
        def Nombre(self):
            return self.__Nombre
        
        @property
        def Apellidos(self):
            return self.__Apellidos
        
        @property
        def Correo(self):
            return self.__Correo
        
        