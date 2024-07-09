class Categoria:
    def __init__(self, id, genero, descripcion):
        self.__id = id
        self.__genero = genero
        self.__descripcion = descripcion

    @property
    def id(self):
        return self.__id

    @property
    def genero(self):
        return self.__genero

    @property
    def descripcion(self):
        return self.__descripcion
