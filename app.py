# Trabajo Práctico I - Programación II

import random
import string
import os

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

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

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

libros=[libro1,libro2,libro3]

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            #completar
            print()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            nuevo_libro()
            print()
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            print("Lista de unidades pretadas:\n")
            for libro in libros:
                if libro["cant_ej_pr"]>0:
                    print(f"Titulo:{libro['titulo']},Autor:{libro['autor']},Cantidad prestada:{libro['cant_ej_pr']}")
                else:
                    print(f"Titulo:{libro['titulo']},Autor:{libro['autor']}, Ninguna unidad prestada")

        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")