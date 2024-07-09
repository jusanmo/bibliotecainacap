from rol_dao import RolDao
from usuario import Usuario
from usuario_dao import UsuarioDao
from libro import Libro
from libro_dao import LibroDao
from categoria import Categoria
from categoria_dao import CategoriaDao
from prestamo import Prestamo
from prestamo_dao import PrestamoDao
from multa import Multa
from multa_dao import MultaDao
from beautifultable import BeautifulTable
import os
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)
daoCategoria = CategoriaDao()
daoLibro = LibroDao()
daoUsuario = UsuarioDao()
daoRol = RolDao()
daoMulta= MultaDao()
daoPrestamo = PrestamoDao()
libro_dao = LibroDao()

def validar_login():
    contraseña_correcta = "12345"
    usuario_correcto = "admin"
    while True:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario != usuario_correcto or contraseña != contraseña_correcta:
            print('Contraseña o usuario incorrecto. Inténtelo nuevamente.')
        else:
            print('Bienvenido Encargado de Biblioteca.')
            break

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para gestionar usuarios
def gestionar_usuarios():
    while True:
        limpiar_pantalla()
        table = BeautifulTable()
        table.columns.header = ['================== GESTIÓN DE USUARIOS ==================']
        table.rows.append(['1. Agregar Usuario'])
        table.rows.append(['2. Modificar Usuario'])
        table.rows.append(['3. Eliminar Usuario'])
        table.rows.append(['4. Listar Usuarios'])
        table.rows.append(['5. Listar Roles'])
        table.rows.append(['6. Volver al Menú Principal'])
        table.column_alignments = BeautifulTable.ALIGN_LEFT
        print(table)

        opcion = input('Seleccione una opción (1-6): ')

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            modificar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            listar_usuarios()
        elif opcion == '5':
            listar_roles()
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            input("Opción inválida. Presione Enter para continuar.")

# Función para listar roles
def listar_roles():
    limpiar_pantalla()
    print('----- Listado de Roles -----')

    try:
        dao_rol = RolDao()
        roles = dao_rol.listarRoles()

        if roles:
            table = BeautifulTable()
            table.columns.header = ['ID', 'Nombre del Rol']
            for rol in roles:
                table.rows.append([rol.id, rol.rol_nombre])
            print(table)
        else:
            print("No hay roles registrados.")
    except Exception as e:
        print(f"Error al listar roles: {str(e)}")

    input("Presione Enter para continuar.")


# Función para agregar usuario
def agregar_usuario():
    limpiar_pantalla()
    print('-----  Agregar Usuario  -----')

    try:
        rut = input('Ingrese el Rut del usuario (sin puntos y con guion): ')
        nombre = input('Ingrese el nombre del usuario: ')
        apellidos = input('Ingrese los apellidos del usuario: ')
        correo = input('Ingrese el correo del usuario: ')
        id_rol = input('Ingrese el ID del rol del usuario(1.Docente y 2. Estudiante): ')

        usuario = Usuario(rut, nombre, apellidos, correo, id_rol)

        dao_usuario = UsuarioDao()
        mensaje = dao_usuario.insertarUsuario(usuario)
        print(mensaje)
    except Exception as e:
        print(f"Error al agregar usuario: {str(e)}")

    input("Presione Enter para continuar.")

# Función para modificar usuario
def modificar_usuario():
    limpiar_pantalla()
    print('-----  Modificar Usuario  -----')

    try:
        dao_usuario = UsuarioDao()
        usuarios = dao_usuario.listarUsuarios()

        if usuarios:
            table = BeautifulTable()
            table.columns.header = ['Rut', 'Nombre', 'Apellidos', 'Correo', 'ID Rol']
            for usuario in usuarios:
                table.rows.append([usuario.rut, usuario.nombre, usuario.apellidos, usuario.correo, usuario.id_rol])
            print(table)
        else:
            print("No hay usuarios registrados.")
            input("Presione Enter para continuar.")
            return

        rut = input('Ingrese el Rut del usuario que desea modificar (sin puntos y con guion): ')
        usuario_actual = dao_usuario.buscarUsuario(rut)

        if not usuario_actual:
            print(f"No se encontró ningún usuario con Rut {rut}.")
            input("Presione Enter para continuar.")
            return

        print(f'Usuario actual: {usuario_actual.nombre} {usuario_actual.apellidos}')

        nuevo_nombre = input(f'Ingrese el nuevo nombre del usuario (actual: {usuario_actual.nombre}): ') or usuario_actual.nombre
        nuevo_apellido = input(f'Ingrese el nuevo apellido del usuario (actual: {usuario_actual.apellidos}): ') or usuario_actual.apellidos
        nuevo_correo = input(f'Ingrese el nuevo correo del usuario (actual: {usuario_actual.correo}): ') or usuario_actual.correo
        nuevo_id_rol = input(f'Ingrese el nuevo ID del rol del usuario (actual: {usuario_actual.id_rol}): ') or usuario_actual.id_rol

        usuario_modificado = Usuario(rut, nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_id_rol)
        mensaje = dao_usuario.modificarUsuario(usuario_modificado)
        print(mensaje)
    except Exception as e:
        print(f"Error al modificar usuario: {str(e)}")

    input("Presione Enter para continuar.")

# Función para eliminar usuario
def eliminar_usuario():
    limpiar_pantalla()
    print('-----  Eliminar Usuario  -----')

    try:
        dao_usuario = UsuarioDao()
        usuarios = dao_usuario.listarUsuarios()

        if usuarios:
            table = BeautifulTable()
            table.columns.header = ['Rut', 'Nombre', 'Apellidos', 'Correo', 'ID Rol']
            for usuario in usuarios:
                table.rows.append([usuario.rut, usuario.nombre, usuario.apellidos, usuario.correo, usuario.id_rol])
            print(table)
        else:
            print("No hay usuarios registrados.")
            input("Presione Enter para continuar.")
            return

        rut = input('Ingrese el Rut del usuario que desea eliminar (sin puntos ni guion): ')

        mensaje = dao_usuario.eliminarUsuario(rut)
        print(mensaje)
    except Exception as e:
        print(f"Error al eliminar usuario: {str(e)}")

    input("Presione Enter para continuar.")

# Función para listar usuarios
def listar_usuarios():
    limpiar_pantalla()
    print('-----  Listado de Usuarios  -----')

    try:
        dao_usuario = UsuarioDao()
        usuarios = dao_usuario.listarUsuarios()

        if usuarios:
            table = BeautifulTable()
            table.columns.header = ['Rut', 'Nombre', 'Apellidos', 'Correo', 'ID Rol']
            for usuario in usuarios:
                table.rows.append([usuario.rut, usuario.nombre, usuario.apellidos, usuario.correo, usuario.id_rol])
            print(table)
        else:
            print("No hay usuarios registrados.")
    except Exception as e:
        print(f"Error al listar usuarios: {str(e)}")

    input("Presione Enter para continuar.")

# Función para gestionar libros
def gestionar_libros():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        table = BeautifulTable()
        table.columns.header = ['================== GESTIÓN DE LIBROS ==================']
        table.rows.append(['1. Agregar Libro'])
        table.rows.append(['2. Modificar Libro'])
        table.rows.append(['3. Eliminar Libro'])
        table.rows.append(['4. Listar Libros'])
        table.rows.append(['5. Volver al Menú Principal'])
        table.column_alignments = BeautifulTable.ALIGN_LEFT
        print(table)

        opcion = input('Seleccione una opción (1-5): ')

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            modificar_libro()
        elif opcion == '3':
            eliminar_libro()
        elif opcion == '4':
            mostrar_libros()
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            input("Opción inválida. Presione Enter para continuar.")

# Función para agregar libro
def mostrar_libros():
    daoLibro = LibroDao()
    libros = daoLibro.listar_libros()

    if libros:
        table = BeautifulTable(maxwidth=120)
        table.set_style(BeautifulTable.STYLE_COMPACT)
        table.columns.header = ['Código', 'Título', 'Descripción', 'Categoría', 'Cantidad']

        for libro in libros:
            # Obtener la categoría del libro
            daoCategoria = CategoriaDao()
            categoria = daoCategoria.buscarCategoria(libro.id_categoria)  # Corregido a buscarCategoria()

            # Agregar una fila a la tabla
            table.rows.append([libro.cod_libro, libro.titulo, libro.descripcion, categoria.genero, libro.cantidad])

        print("Libros existentes:")
        print(table)
    else:
        print("No hay libros registrados.")

    # Mensaje para continuar
    input("\nPresiona Enter para volver al menú de gestión de libros...")

def agregar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Agregar Libro  -----')

    # Mostrar libros existentes antes de agregar uno nuevo
    mostrar_libros()

    cod_libro = input('Ingrese el código del libro: ')
    titulo = input('Ingrese el título del libro: ')
    descripcion = input('Ingrese la descripción del libro: ')
    
    # Mostrar las categorías existentes
    listar_categorias()

    while True:
        id_categoria = int(input('Ingrese el ID de la categoría del libro o 0 para agregar una nueva con ID personalizado: '))

        if id_categoria == 0:
            # Solicitar ID personalizado para la nueva categoría
            id_categoria_personalizado = int(input('Ingrese el ID personalizado para la nueva categoría: '))

            # Validar si el ID personalizado ya existe
            daoCategoria = CategoriaDao()
            categoria_existente = daoCategoria.buscarCategoria(id_categoria_personalizado)
            if categoria_existente:
                print(f"Ya existe una categoría con el ID {id_categoria_personalizado}. Intente con otro ID.")
                continue

            # Agregar una nueva categoría con ID personalizado
            genero = input('Ingrese el género de la nueva categoría: ')
            descripcion_cat = input('Ingrese la descripción de la nueva categoría: ')
            
            # Crear la nueva categoría con ID personalizado
            nueva_categoria = Categoria(id_categoria_personalizado, genero, descripcion_cat)
            mensaje_nueva_cat = daoCategoria.insertarCategoria(nueva_categoria)
            print(mensaje_nueva_cat)
            
            # Volver a mostrar las categorías actualizadas
            listar_categorias()
            break
        else:
            # Buscar la categoría por su ID
            daoCategoria = CategoriaDao()
            categoria = daoCategoria.buscarCategoria(id_categoria)
            if not categoria:
                print("Categoría no encontrada.")
            else:
                break

    cantidad = int(input('Ingrese la cantidad del libro: '))

    # Crear el objeto Libro con los datos proporcionados
    libro = Libro(cod_libro, titulo, descripcion, id_categoria, cantidad)

    # Insertar el libro en la base de datos
    daoLibro = LibroDao()
    mensaje = daoLibro.insertarLibro(libro)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para modificar libro
def modificar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Modificar Libro  -----')

    mostrar_libros()  # Mostrar los libros existentes

    cod_libro = input('Ingrese el código del libro que desea modificar: ')
    daoLibro = LibroDao()
    libro_actual = daoLibro.buscarLibroPorCodigo(cod_libro)

    if not libro_actual:
        print(f"No se encontró ningún libro con código {cod_libro}.")
        input("Presione Enter para continuar.")
        return

    print(f'Libro actual: {libro_actual.titulo}')

    print("Modifique los campos que desee. Deje en blanco para mantener el valor actual.")

    nuevo_titulo = input(f'Ingrese el nuevo título del libro ({libro_actual.titulo}): ') or libro_actual.titulo
    nueva_descripcion = input(f'Ingrese la nueva descripción del libro ({libro_actual.descripcion}): ') or libro_actual.descripcion

    daoCategoria = CategoriaDao()
    categorias = daoCategoria.listarCategorias()

    print("Categorías existentes:")
    for categoria in categorias:
        print(f"ID: {categoria.id} - Género: {categoria.genero} - Descripción: {categoria.descripcion}")

    while True:
        nueva_cantidad = input(f'Ingrese el nuevo ID de la categoría ({libro_actual.cantidad}): ')
        if nueva_cantidad == '':
            nueva_cantidad = libro_actual.cantidad
            break
        try:
            nueva_cantidad = int(nueva_cantidad)
            if nueva_cantidad >= 0:
                break
            else:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
        except ValueError:
            print("Ingrese un número válido para la cantidad.")

    while True:
        nuevo_id_categoria = input(f'Ingrese la nueva cantidad del libro ({libro_actual.id_categoria}): ')
        if nuevo_id_categoria == '':
            nuevo_id_categoria = libro_actual.id_categoria
            break
        try:
            nuevo_id_categoria = int(nuevo_id_categoria)
            if daoCategoria.buscarCategoria(nuevo_id_categoria):
                break
            else:
                print("ID de categoría no válido. Intente nuevamente.")
        except ValueError:
            print("Ingrese un número válido para el ID de la categoría.")

    libro_modificado = Libro(cod_libro, nuevo_titulo, nueva_descripcion, nuevo_id_categoria, nueva_cantidad)
    mensaje = daoLibro.modificarLibro(libro_modificado)
    print(mensaje)
    input("Presione Enter para continuar.")


# Función para eliminar libro
def eliminar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Eliminar Libro  -----')

    # Mostrar libros existentes antes de solicitar el ID del libro a eliminar
    mostrar_libros()

    id_libro = input('Ingrese el código del libro que desea eliminar: ')

    daoLibro = LibroDao()
    mensaje = daoLibro.eliminarLibro(id_libro)
    print(mensaje)
    input("Presione Enter para continuar.")



# Función para gestionar categorías
def gestionar_categorias():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        table = BeautifulTable()
        table.columns.header = ['================== GESTIÓN DE CATEGORÍAS ==================']
        table.rows.append(['1. Agregar Categoría'])
        table.rows.append(['2. Modificar Categoría'])
        table.rows.append(['3. Eliminar Categoría'])
        table.rows.append(['4. Listar Categorías'])
        table.rows.append(['5. Volver al Menú Principal'])
        table.column_alignments = BeautifulTable.ALIGN_LEFT
        print(table)

        opcion = input('Seleccione una opción (1-5): ')

        if opcion == '1':
            agregar_categoria()
        elif opcion == '2':
            modificar_categoria()
        elif opcion == '3':
            eliminar_categoria()
        elif opcion == '4':
            listar_categorias()
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            input("Opción inválida. Presione Enter para continuar.")

# Función para agregar categoría
def agregar_categoria():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Agregar Categoría  -----')

    listar_categorias()  # Mostrar categorías existentes

    id = int(input('Ingrese el ID de la categoría: '))
    genero = input('Ingrese el género de la categoría: ')
    descripcion = input('Ingrese la descripción de la categoría: ')

    categoria = Categoria(id, genero, descripcion)

    daoCategoria = CategoriaDao()
    mensaje = daoCategoria.insertarCategoria(categoria)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para modificar categoría
def modificar_categoria():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Modificar Categoría  -----')

    listar_categorias()  # Mostrar categorías existentes

    id = int(input('Ingrese el ID de la categoría que desea modificar: '))
    daoCategoria = CategoriaDao()
    categoria_actual = daoCategoria.buscarCategoria(id)

    if not categoria_actual:
        print(f"No se encontró ninguna categoría con ID {id}.")
        input("Presione Enter para continuar.")
        return

    print(f'Categoría actual: {categoria_actual.genero} - {categoria_actual.descripcion}')

    nuevo_genero = input(f'Ingrese el nuevo género de la categoría (actual: {categoria_actual.genero}): ') or categoria_actual.genero
    nueva_descripcion = input(f'Ingrese la nueva descripción de la categoría (actual: {categoria_actual.descripcion}): ') or categoria_actual.descripcion

    categoria_modificada = Categoria(id, nuevo_genero, nueva_descripcion)
    mensaje = daoCategoria.modificarCategoria(categoria_modificada)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para eliminar categoría
def eliminar_categoria():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Eliminar Categoría  -----')

    daoCategoria = CategoriaDao()
    categorias = daoCategoria.listarCategorias()

    if categorias:
        table = BeautifulTable()
        table.columns.header = ['ID', 'Género', 'Descripción']
        for categoria in categorias:
            table.rows.append([categoria.id, categoria.genero, categoria.descripcion])
        print(table)
    else:
        print("No hay categorías registradas.")
        input("Presione Enter para continuar.")
        return

    id_categoria = int(input('Ingrese el ID de la categoría que desea eliminar: '))

    mensaje = daoCategoria.eliminarCategoria(id_categoria)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para listar categorías
def listar_categorias():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Listado de Categorías  -----')

    daoCategoria = CategoriaDao()
    categorias = daoCategoria.listarCategorias()

    if categorias:
        table = BeautifulTable()
        table.columns.header = ['ID', 'Género', 'Descripción']
        for categoria in categorias:
            table.rows.append([categoria.id, categoria.genero, categoria.descripcion])
        print(table)
    else:
        print("No hay categorías registradas.")

    input("Presione Enter para continuar.")

# Función para gestionar préstamos
def gestionar_prestamos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        table = BeautifulTable()
        table.columns.header = ['================== GESTIÓN DE PRÉSTAMOS ==================']
        table.rows.append(['1. Realizar Préstamo'])
        table.rows.append(['2. Renovar Préstamo'])
        table.rows.append(['3. Devolver Libro'])
        table.rows.append(['4. Listar Préstamos'])
        table.rows.append(['5. Volver al Menú Principal'])
        table.column_alignments = BeautifulTable.ALIGN_LEFT
        print(table)

        opcion = input('Seleccione una opción (1-5): ')

        if opcion == '1':
            realizar_prestamo()
        elif opcion == '2':
            renovar_prestamo()
        elif opcion == '3':
            devolver_libro()
        elif opcion == '4':
            listar_prestamos()
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            input("Opción inválida. Presione Enter para continuar.")

# Función para realizar préstamo
def realizar_prestamo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Realizar Préstamo  -----')

    rut_usuario = input('Ingrese el Rut del usuario que solicita el préstamo (sin puntos ni guion): ')
    cod_libro = input('Ingrese el Código del libro que se desea prestar: ')

    daoUsuario = UsuarioDao()
    usuario = daoUsuario.buscar_usuario_por_rut(rut_usuario)
    if not usuario:
        print("Usuario no encontrado.")
        input("Presione Enter para continuar.")
        return

    daoLibro = LibroDao()
    libro = daoLibro.buscar_libro_por_codigo(cod_libro)
    if not libro:
        print("Libro no encontrado.")
        input("Presione Enter para continuar.")
        return

    hoy = datetime.now()
    fecha_devolucion = hoy + timedelta(days=7)  # Préstamo por defecto de 7 días

    # Si el usuario es docente, se extiende el préstamo a 20 días
    if usuario.id_rol == 1:  # Suponiendo que el id_rol 1 es para docentes
        fecha_devolucion = hoy + timedelta(days=20)

    prestamo = Prestamo(None, rut_usuario, cod_libro, hoy, fecha_devolucion)

    daoPrestamo = PrestamoDao()
    mensaje = daoPrestamo.realizarPrestamo(prestamo)  # Llamada correcta
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para renovar préstamo
def renovar_prestamo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Renovar Préstamo  -----')

    daoPrestamo = PrestamoDao()

    # Listar los préstamos existentes para que el usuario seleccione uno
    listar_prestamos()

    # Solicitar al usuario el ID del préstamo que desea renovar
    id_prestamo = int(input('Ingrese el ID del préstamo que desea renovar: '))

    # Buscar el préstamo por su ID
    prestamo_actual = daoPrestamo.buscarPrestamo(id_prestamo)

    if not prestamo_actual:
        print(f"No se encontró ningún préstamo con ID {id_prestamo}.")
        input("Presione Enter para continuar.")
        return

    hoy = datetime.now()

    if prestamo_actual.fecha_devolucion < hoy.date():
        print("No se puede renovar el préstamo porque ya está vencido.")
        input("Presione Enter para continuar.")
        return

    # Calcular la nueva fecha de devolución (3 días adicionales)
    nueva_fecha_devolucion = prestamo_actual.fecha_devolucion + timedelta(days=3)

    # Actualizar la fecha de devolución en el objeto Prestamo
    prestamo_actual.fecha_devolucion = nueva_fecha_devolucion

    # Lógica para actualizar el préstamo en la base de datos (o donde corresponda)
    mensaje = daoPrestamo.renovarPrestamo(prestamo_actual)
    print(mensaje)
    input("Presione Enter para continuar.")
    
# Función para devolver libro
def devolver_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Devolver Libro  -----')

    # Crear una instancia de PrestamoDao
    daoPrestamo = PrestamoDao()

    # Listar los préstamos activos
    prestamos_activos = daoPrestamo.listar_prestamos_activos()

    if not prestamos_activos:
        print("No hay préstamos activos para devolver.")
        input("Presione Enter para continuar.")
        return

    # Mostrar los préstamos activos
    print("Préstamos activos:")
    for prestamo in prestamos_activos:
        print(f"ID: {prestamo.id}, Libro: {prestamo.cod_libro}, Usuario: {prestamo.rut_usuario}, Fecha Devolución: {prestamo.fecha_devolucion}")

    id_prestamo = int(input('Ingrese el ID del préstamo que desea devolver: '))

    mensaje = daoPrestamo.devolverLibro(id_prestamo)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para listar préstamos
def listar_prestamos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Listado de Préstamos  -----')

    daoPrestamo = PrestamoDao()
    prestamos = daoPrestamo.listarPrestamos()

    if prestamos:
        table = BeautifulTable()
        table.columns.header = ['ID', 'Usuario', 'Libro', 'Fecha Préstamo', 'Fecha Devolución', 'Estado']
        hoy = datetime.now().date()  # Obtener solo la fecha actual sin la parte de la hora
        for prestamo in prestamos:
            estado = 'Vencido' if prestamo['fecha_devolucion'] < hoy else 'Activo'  # Comparar directamente con hoy que es un datetime.date
            table.rows.append([prestamo['id'], f"{prestamo['usuario']['nombre']} {prestamo['usuario']['apellidos']} ({prestamo['usuario']['rut']})", prestamo['libro']['titulo'], prestamo['fecha_prestamo'].strftime('%Y-%m-%d'), prestamo['fecha_devolucion'].strftime('%Y-%m-%d'), estado])
        print(table)
    else:
        print("No hay préstamos registrados.")

    input("Presione Enter para continuar.")
# Función para gestionar multas
def gestionar_multas():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        table = BeautifulTable()
        table.columns.header = ['================== GESTIÓN DE MULTAS ==================']
        table.rows.append(['1. Registrar Multa'])
        table.rows.append(['2. Pagar Multa'])
        table.rows.append(['3. Listar Multas'])
        table.rows.append(['4. Volver al Menú Principal'])
        table.column_alignments = BeautifulTable.ALIGN_LEFT
        print(table)

        opcion = input('Seleccione una opción (1-4): ')

        if opcion == '1':
            registrar_multa()
        elif opcion == '2':
            pagar_multa()
        elif opcion == '3':
            listar_multas()
        elif opcion == '4':
            print("Volviendo al menú principal...")
            break
        else:
            input("Opción inválida. Presione Enter para continuar.")

# Función para registrar multa
def registrar_multa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Registrar Multa  -----')

    rut_usuario = input('Ingrese el Rut del usuario que tiene la multa (sin puntos ni guion): ')
    cod_libro = input('Ingrese el Código del libro asociado a la multa: ')
    dias_retraso = int(input('Ingrese los días de retraso: '))

    # Validar que el usuario existe
    daoUsuario = UsuarioDao()
    usuario = daoUsuario.buscarUsuario(rut_usuario)
    if not usuario:
        print("Usuario no encontrado.")
        input("Presione Enter para continuar.")
        return

    # Validar que el libro existe
    daoLibro = LibroDao()
    libro = daoLibro.buscarLibro(cod_libro)
    if not libro:
        print("Libro no encontrado.")
        input("Presione Enter para continuar.")
        return

    # Calcular el monto de la multa
    monto_multa = dias_retraso * 1000

    multa = Multa(None, rut_usuario, cod_libro, dias_retraso, monto_multa, False)

    daoMulta = MultaDao()
    mensaje = daoMulta.registrar_multa(multa)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para pagar multa
def pagar_multa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Pagar Multa  -----')

    daoMulta = MultaDao()
    multas = daoMulta.listar_multas()  # Listar todas las multas antes de solicitar el ID

    if not multas:
        print("No hay multas registradas.")
        input("Presione Enter para continuar.")
        return

    table = BeautifulTable()
    table.columns.header = ['ID', 'Código del Libro', 'Días de Retraso', 'Monto', 'Pagada']
    for multa in multas:
        estado_pagada = "Pagada" if multa.pagada else "No Pagada"
        table.rows.append([multa.id_multa, multa.cod_libro, multa.dias_retraso, f"${multa.monto}", estado_pagada])
    print(table)

    id_multa = int(input('Ingrese el ID de la multa que desea pagar (0 para cancelar): '))

    if id_multa == 0:
        print("Cancelando operación.")
        input("Presione Enter para continuar.")
        return

    multa = daoMulta.buscar_multa_por_id(id_multa)

    if not multa:
        print(f"No se encontró ninguna multa con ID {id_multa}.")
        input("Presione Enter para continuar.")
        return

    if multa.pagada:
        print(f"La multa con ID {id_multa} ya ha sido pagada.")
        input("Presione Enter para continuar.")
        return

    # Marcar la multa como pagada
    mensaje = daoMulta.marcar_multa_pagada(id_multa)
    print(mensaje)
    input("Presione Enter para continuar.")

# Función para listar multas
def listar_multas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-----  Listado de Multas  -----')

    daoMulta = MultaDao()
    multas = daoMulta.listar_multas()

    if multas:
        table = BeautifulTable()
        table.columns.header = ['ID', 'Usuario', 'Libro', 'Días de Retraso', 'Monto', 'Pagada']
        
        # Iterar sobre cada multa y obtener detalles adicionales si es necesario
        for multa in multas:
            # Obtener el nombre del usuario asociado a la multa
            daoUsuario = UsuarioDao()
            usuario = daoUsuario.buscar_usuario_por_rut(multa.rut_usuario)
            nombre_usuario = f"{usuario.nombre} ({usuario.rut})" if usuario else multa.rut_usuario

            # Obtener los detalles del libro asociado a la multa
            daoLibro = LibroDao()
            libro = daoLibro.buscar_libro_por_codigo(multa.cod_libro)
            titulo_libro = libro.titulo if libro else multa.cod_libro

            estado_pagada = "Pagada" if multa.pagada else "No Pagada"
            table.rows.append([multa.id_multa, nombre_usuario, titulo_libro, multa.dias_retraso, f"${multa.monto}", estado_pagada])
        
        print(table)
    else:
        print("No hay multas registradas.")

    input("Presione Enter para continuar.")

# Función principal
def main():
    #validar_login()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        table = BeautifulTable()
        table.columns.header = ['================== MENÚ PRINCIPAL ==================']
        table.rows.append(['1. Gestionar Usuarios'])
        table.rows.append(['2. Gestionar Libros'])
        table.rows.append(['3. Gestionar Categorías'])
        table.rows.append(['4. Gestionar Préstamos'])
        table.rows.append(['5. Gestionar Multas'])
        table.rows.append(['6. Salir'])
        table.column_alignments = BeautifulTable.ALIGN_LEFT
        print(table)

        opcion = input('Seleccione una opción (1-6): ')

        if opcion == '1':
            gestionar_usuarios()
        elif opcion == '2':
            gestionar_libros()
        elif opcion == '3':
            gestionar_categorias()
        elif opcion == '4':
            gestionar_prestamos()
        elif opcion == '5':
            gestionar_multas()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            input("Opción inválida. Presione Enter para continuar.")

if __name__ == "__main__":
    main()
