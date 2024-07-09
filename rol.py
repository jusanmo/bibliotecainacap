class Rol:
    def __init__(self, id, rol_nombre):
        self.__id = id
        self.__rol_nombre = rol_nombre

    @property
    def id(self):
        return self.__id

    @property
    def rol_nombre(self):
        return self.__rol_nombre
