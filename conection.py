import mysql.connector

class Conexion:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'biblioteca'
        self.conexion = None
        self.cursor = None
    
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(f"Error al conectar a MySQL: {str(e)}")
    
    def cerrar(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.conexion is not None:
                self.conexion.close()
        except Exception as e:
            print(f"Error al cerrar conexión MySQL: {str(e)}")