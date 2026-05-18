from catalogoDeLibros.catalogo_de_libros import *

# Menu principal del programa

while True:
    print("----------------------------------------------------------------------\n")
    print("|           Biblioteca Popular El Aljibe - Sistema v1.0               |\n")
    print("----------------------------------------------------------------------\n")
    print("|                                                                     |\n")
    print("|                     1. Catalogo de libros                           |\n")
    print("|                     2. Socios                                       |\n")
    print("|                     3. Préstamos                                    |\n")
    print("|                     4. Reservas                                     |\n")
    print("|                     5. Donaciones recibidas                         |\n")
    print("|                                                                     |\n")
    print("|                     0. Salir                                        |\n")
    print("|                                                                     |\n")
    print("----------------------------------------------------------------------\n")

    opcion_ingresada = input("|                     ¿Qué queres hacer?                              |\n\n")
    
    match (opcion_ingresada):
        case "0":
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n  ... Saliendo del programa. Hasta luego!\n\n")
            break
        case "1":
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n")
            menu_principal_libros()

        case "2":
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

        case "3":
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

        case "4":
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

        case "5":
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

        case _:
            print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 
            print("Opcion inválida\n")
