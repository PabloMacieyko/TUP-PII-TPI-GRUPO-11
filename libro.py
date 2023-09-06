import random
import string

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

libros=[libro1,libro2,libro3]

def generar():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod

def nuevo_libro():
    libro={"cod": "","cant_ej_ad":0,'cant_ej_pr': 0, "titulo": "", "autor": ""}
    libro["cod"]=generar()
    libro["cant_ej_ad"]=input("ingrese la cantidad de ejemplares:\n")
    libro["cant_ej_pr"]=0
    libro["titulo"]=input("ingrese el titulo:\n")
    libro["autor"]=input("ingrese el autor:\n")
    libros.append(libro)
    return None

nuevo_libro()
print (libros)


