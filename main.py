from prestamo_dao import PrestamoDao
from prestamo import Prestamo
from os import system 
from estudiante import Estudiante
from beautifultable import BeautifulTable

system('cls')

menu = BeautifulTable()

menu.columns._header = ['============================ MENU DE OPCIONES ============================']
menu.rows.append(['1.Realizar prestamo'])
menu.rows.append(['2.Agregar estudiante'])
menu.rows.append(['2.Agregar docente'])


def realizarPrestamo():
    system ('cls')
    print('------- Ingrese el codigo del libro para saber si esta en prestamo -------')
    libro = int(input('Codigo del libro: '))
    if PrestamoDao.insertarPrestamo(libro) != None:



