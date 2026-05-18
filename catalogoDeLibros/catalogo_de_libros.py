# Parte del programa que se encarga de los libros

def menu_principal_libros():
    while True:
        print("----------------------------------------------------------------------\n")
        print("|           Biblioteca Popular El Aljibe - Sistema v1.0               |\n")
        print("----------------------------------------------------------------------\n")
        print("|                                                                     |\n")
        print("|                              MENU                                   |\n")
        print("|                 ----  Catalogo de Libros  ----                      |\n")
        print("|                                                                     |\n")
        print("|                     1. Catalogo completo de libros                  |\n")
        print("|                     2. Buscar libro                                 |\n")
        print("|                     3. Filtrar por estado                           |\n")
        print("|                     4. Cargar un libro                              |\n")
        print("|                     5. Cambiar estado de libro                      |\n")
        print("|                     6. Dar de baja un libro                         |\n")
        print("|                                                                     |\n")
        print("|                     9. Salir                                        |\n")
        print("|                                                                     |\n")
        print("----------------------------------------------------------------------\n")

        opcion_ingresada = input("|                     ¿Qué queres hacer?                              |\n\n")
    
        match (opcion_ingresada):
            case "9":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n")
                break
            case "1":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

            case "2":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

            case "3":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

            case "4":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 

            case "5":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n")
        
            case "6":
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n")

            case _:
                print(f"    Opcion ingresada: --> {opcion_ingresada}\n") 
                print("Opcion inválida\n")