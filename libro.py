import cod_generator

# Crear un diccionario para cada libro

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1,
          "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2,
          "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0,
          "titulo": "El código Da Vinci", "autor": "Dan Brown"}


def nuevo_libro():
    nuevo_libro = {}
    nuevo_libro['cod'] = cod_generator.generar()
    nuevo_libro['cant_ej_ad'] = int(input("Ingrese la cantidad de ejemplares adquiridos: "))
    nuevo_libro['cant_ej_pr'] = 0
    nuevo_libro['titulo'] = input("Ingrese el título del libro: ")
    nuevo_libro['autor'] = input("Ingrese el nombre del autor: ")
    return nuevo_libro

def generar_codigo():
    return cod_generator.generar()