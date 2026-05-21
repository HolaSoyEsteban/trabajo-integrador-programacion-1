import os
from catalogoDeLibros.catalogo_de_libros import menu_principal_libros

# Colores ANSI para la consola
RESET = "\033[0m"
NEGRITA = "\033[1m"
CELESTE = "\033[1;36m"
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
GRIS = "\033[90m"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    limpiar_pantalla()
    print(f"{CELESTE}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CELESTE}║{RESET}  {NEGRITA} BIBLIOTECA POPULAR EL ALJIBE — Sistema de Gestión{RESET}  {CELESTE}║{RESET}")
    print(f"{CELESTE}╠════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}1.{RESET} Catálogo de libros                                            {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}2.{RESET} Socios                                                         {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}3.{RESET} Préstamos                                                      {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}4.{RESET} Reservas                                                       {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}5.{RESET} Donaciones recibidas                                           {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}0.{RESET} Salir del sistema                                              {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}╚════════════════════════════════════════════════════════════════════╝{RESET}")

def ejecutar_sistema():
    while True:
        mostrar_menu_principal()
        opcion = input(f"\n{AMARILLO}¿Qué querés hacer? (0-5): {RESET}").strip()
        if opcion == "0":
            limpiar_pantalla()
            print(f"\n{VERDE}¡Gracias por usar el sistema! Saliendo del programa. ¡Hasta luego!{RESET}\n")
            break
        elif opcion == "1":
            menu_principal_libros()
        elif opcion in ["2", "3", "4", "5"]:
            input(f"\n{CELESTE}[INFO]{RESET} El módulo '{opcion}' estará disponible próximamente.\nPresione Enter para volver...")
        else:
            input(f"\n{ROJO}[ERROR] Opción inválida. Presione Enter para reintentar...{RESET}")

if __name__ == "__main__":
    ejecutar_sistema()
