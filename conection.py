import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inacap",
            port="3306"
        )
        self.cursor = self.conexion.cursor()

    def connection(self):
        return self.conexion
    
    def cursor(self):
        return self.cursor