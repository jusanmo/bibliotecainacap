class Libro:
    def __init__(self, cod_libro, titulo, descripcion, id_categoria, cantidad):
        self.__cod_libro = cod_libro
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__id_categoria = id_categoria
        self.__cantidad = cantidad

    @property
    def cod_libro(self):
        return self.__cod_libro

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def id_categoria(self):
        return self.__id_categoria

