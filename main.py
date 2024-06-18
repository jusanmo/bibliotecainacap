from usuario import Usuario
from usuario_dao import UsuarioDao
from beautifultable import BeautifulTable
from os import system
import time
import os
system('cls')

daousuario = UsuarioDao()

menu = BeautifulTable()

menu.columns._header = ['============================ MENU DE OPCIONES ============================']
menu.rows.append(['1.Agregar Usuario'])
menu.rows.append(['2.Salir'])
menu.rows.append(['3.Agregar Multa'])
menu.column_alignments = BeautifulTable.ALIGN_LEFT

time.sleep(5)
while True:
    os.system("cls")
    print(menu)
    option = input('Opcion: ')
    if option == '1':
        os.system('cls')
        print('-----  Agregar Usuario  -----')
        rut = input('Rut(Con guion): ')
        nombre = input('Nombre: ')
        apellidos = input('Apellidos: ')
        correo = input("Correo: ")
        print(daousuario.insertarUsuario(Usuario(rut, nombre, apellidos, correo)))
        time.sleep(5)
    elif option == '2':
        os.system('cls')
        print ("Bye Bye")
        time.sleep(5)
    else: os






