import os

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

def mostrar_menu_socios():
    limpiar_pantalla()
    print(f"{CELESTE}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CELESTE}║{RESET}  {NEGRITA}GESTIÓN DE SOCIOS — Biblioteca Popular El Aljibe  {RESET}{CELESTE}                ║{RESET}")
    print(f"{CELESTE}╠════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}1.{RESET} Listar todos los socios                                       {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}2.{RESET} Consultar ficha de socio (Buscar e historial)                 {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}3.{RESET} Registrar socio nuevo                                         {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}4.{RESET} Actualizar datos de contacto                                  {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}5.{RESET} Dar de baja a un socio                                        {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}9.{RESET} Volver al menú principal                                      {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}╚════════════════════════════════════════════════════════════════════╝{RESET}")

def menu_principal_socios():
    while True:
        mostrar_menu_socios()
        opcion = input(f"\n{AMARILLO}¿Qué querés hacer? (1-5, 9): {RESET}").strip()
        if opcion == "9":
            break
        elif opcion == "1":
            #listar_socios_completo()
            pass
        elif opcion == "2":
            #buscar_socio_detalle()
            pass
        elif opcion == "3":
            #registrar_socio()
            pass
        elif opcion == "4":
            #actualizar_datos_contacto()
            pass
        elif opcion == "5":
            #dar_de_baja_socio()
            pass
        else:
            print(f"\n{ROJO}Opción inválida.{RESET}")
            
        input(f"\n{GRIS}Presione Enter para continuar...{RESET}")