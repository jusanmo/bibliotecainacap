class Multa:
    def __init__(self, id_multa, rut_usuario, cod_libro, dias_retraso, monto, pagada):
        self.__id_multa = id_multa
        self.__rut_usuario = rut_usuario
        self.__cod_libro = cod_libro
        self.__dias_retraso = dias_retraso
        self.__monto = monto
        self.__pagada = pagada

    @property
    def id_multa(self):
        return self.__id_multa

    @property
    def rut_usuario(self):
        return self.__rut_usuario

    @property
    def cod_libro(self):
        return self.__cod_libro

    @property
    def dias_retraso(self):
        return self.__dias_retraso

    @property
    def monto(self):
        return self.__monto

    @property
    def pagada(self):
        return self.__pagada