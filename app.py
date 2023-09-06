# Trabajo Práctico I - Programación II


import os
import biblioteca


print("Bienvenido a la biblioteca Jose Manuel Estrada!")
respuesta = ''


def menu():
    print("1 - Gestionar Préstamo.")
    print("2 - Gestionar Devolución.")
    print("3 - Registrar Nuevo Libro.")
    print("4 - Elimiar ejemplar.")
    print("5 - Mostrar ejemplares prestados.")
    print("6 - Salir.")


while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")  # Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            biblioteca.gestionar_prestamo()
            print()
        elif int(opt) == 2:
            biblioteca.gestionar_devolucion()
            print()
        elif int(opt) == 3:
            biblioteca.registrar_nuevo_libro()
            print()
        elif int(opt) == 4:
            biblioteca.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            biblioteca.mostrar_ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")

    input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!.")
