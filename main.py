from prestamo_dao import PrestamoDao
from prestamo import Prestamo
from os import system 
from beautifultable import BeautifulTable

system('cls')

menu = BeautifulTable()

menu.columns._header = ['============================ MENU DE OPCIONES ============================']
menu.rows.append(['1.Realizar prestamo'])
menu.rows.append([''])