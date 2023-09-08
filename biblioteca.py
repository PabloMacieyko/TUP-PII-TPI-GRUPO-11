import libro

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(libro.libro1)
libros.append(libro.libro2)
libros.append(libro.libro3)

def mostrar_ejemplares_prestados():
    print("Lista de unidades prestadas:\n")
    for libro in libros:
        if libro["cant_ej_pr"]>0:
            print(f"Titulo:{libro['titulo']},Cantidad prestada:{libro['cant_ej_pr']}")
        else:
            print(f"Titulo:{libro['titulo']}, Ninguna unidad prestada")
    return None

def registrar_nuevo_libro():
    nuevo_libro = libro.nuevo_libro()
    libros.append(nuevo_libro)
    print("!Libro resgristrado con éxito!")
    return None

def eliminar_ejemplar_libro():
    cod = input("Ingrese el codigo del libro a eliminar: ")
    for libro in libros:
        if libro['cod'] == cod:
            libros.remove(libro)
            print("¡Ejemplar eliminado con éxito!")
            break
    else:
        print("¡Código de libro incorrecto o no encontrado!")
    return None

def gestionar_prestamo():
    libros_disponibles()
    codigo_libro = input("Ingrese el código del libro que desea prestar: ")

    libro_encontrado = None
    for libro in libros:
        if libro['cod'] == codigo_libro and libro['cant_ej_pr'] > 0:
            libro_encontrado = libro
            break

    if libro_encontrado:
        print(f"Título del libro encontrado: {libro_encontrado['titulo']} - Autor: {libro_encontrado['autor']}")
        confirmar_prestamo = input("¿Desea confirmar el préstamo? (Presione 's' para confirmar): ").lower()
        if confirmar_prestamo == 's':
            libro_encontrado['cant_ej_pr'] += 1
            print("¡Préstamo confirmado!")
        else:
            print("Préstamo cancelado.")
    else:
        print("Código incorrecto o no hay ejemplares disponibles en este momento.")
    return None

def gestionar_devolucion():
    codigo_libro = input("Ingrese el código del libro que va a devolver: ")

    libro_encontrado = None
    for libro in libros:
        if libro['cod'] == codigo_libro and libro['cant_ej_pr'] > 0:
           libro_encontrado = libro
           break
       
    if libro_encontrado:
       print(f"Título del libro encontrado: {libro_encontrado['titulo']} - Autor: {libro_encontrado['autor']}")
       confirmar_devolucion = input("¿Desea confirmar la devolución? (Presione 's' para confirmar): ").lower()
       if confirmar_devolucion == 's':
           libro_encontrado['cant_ej_pr'] -= 1
           print("Devolución confirmada. ¡Gracias por devolver el libro!")
       else:
            print("Devolución cancelada.")
    else:
       print("¡Código incorrecto o no hay ejemplares prestados!")


def libros_disponibles():
    disponibles = []
    for libro in libros:
        if libro['cant_ej_ad'] > 0:
            disponibles.append(libro)
    if disponibles:
        print("Libros disponibles: ")
        for libro in disponibles:
            print(f"Código: {libro['cod']}")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Ejemplares disponibles: {libro['cant_ej_ad']-libro['cant_ej_pr']}")
    else:
        print("No hay libros disponibles en este momento.")
