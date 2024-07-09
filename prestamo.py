class Prestamo:
    def __init__(self, id, rut_usuario, cod_libro, fecha_prestamo, fecha_devolucion):
        self.__id = id
        self.__rut_usuario = rut_usuario
        self.__cod_libro = cod_libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

    @property
    def id(self):
        return self.__id

    @property
    def rut_usuario(self):
        return self.__rut_usuario

    @property
    def cod_libro(self):
        return self.__cod_libro

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo

    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha_devolucion):
        self.__fecha_devolucion = nueva_fecha_devolucion