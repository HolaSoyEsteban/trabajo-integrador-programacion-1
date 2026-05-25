import os
from datetime import datetime

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
            listar_socios_completo()
        elif opcion == "2":
            buscar_socio_detalle()
        elif opcion == "3":
            registrar_socio()
        elif opcion == "4":
            #actualizar_datos_contacto()
            pass
        elif opcion == "5":
            #dar_de_baja_socio()
            pass
        else:
            print(f"\n{ROJO}Opción inválida.{RESET}")

        input(f"\n{GRIS}Presione Enter para continuar...{RESET}")

# Lista de socios hasta tener el archivo JSON con los datos
lista_socios = [
    {
        "nro_carnet": 1, "dni": "14234567", "nombre": "Alberto Gómez",
        "telefono": "11-4444-5555", "email": "No posee", "fecha_alta": "22/05/2026",
        "categoria": "jubilado", "estado": "activo",
        "prestamos_actuales": ["Cien años de soledad"], 
        "historial_prestamos": ["Cien años de soledad", "El Aleph"]
    },
    {
        "nro_carnet": 2, "dni": "45123890", "nombre": "Martina Rodríguez",
        "telefono": "3442-654321", "email": "martina@email.com", "fecha_alta": "23/05/2026",
        "categoria": "estudiante", "estado": "activo",
        "prestamos_actuales": [], 
        "historial_prestamos": ["Rayuela"]
    },
    {
        "nro_carnet": 3, "dni": "28456123", "nombre": "Carlos Pérez",
        "telefono": "11-9876-5432", "email": "carlos.perez@email.com", "fecha_alta": "24/05/2026",
        "categoria": "general", "estado": "dado de baja",
        "prestamos_actuales": [], 
        "historial_prestamos": []
    },
    {
        "nro_carnet": 4, "dni": "78789789", "nombre": "Morgan Stark",
        "telefono": "11-0000-0000", "email": "morganstark@email.com", "fecha_alta": "25/05/2026",
        "categoria": "infantil", "estado": "activo",
        "prestamos_actuales": ["Drácula","Frankenstein"], 
        "historial_prestamos": []
    }
]

ultimo_carnet = lista_socios[-1]["nro_carnet"] if lista_socios else 0

def mostrar_tabla_socios(socios):
    if not socios:
        print(f"\n{ROJO}No se encontraron socios para mostrar.{RESET}\n")
        return
    border = f"{CELESTE}" + "-" * 115 + f"{RESET}"
    print(border)
    print(f"{NEGRITA}{'Carnet':<8} | {'DNI':<10} | {'Nombre Completo':<25} | {'Teléfono':<15} | {'Categoría':<12} | {'Alta':<12} | {'Estado'}{RESET}")
    print(border)
    for socio in socios:
        nombre_completo = socio["nombre"][:23] + ".." if len(socio["nombre"]) > 25 else socio["nombre"]
        estado = socio["estado"]
        estado_padded = f"{estado:<12}"
        if estado == "activo":
            estado_color = f"{VERDE}{estado_padded}{RESET}"
        else:
            estado_color = f"{ROJO}{estado_padded}{RESET}"
            
        print(f"{socio['nro_carnet']:<8} | {socio['dni']:<10} | {nombre_completo:<25} | {socio['telefono']:<15} | {socio['categoria']:<12} | {socio['fecha_alta']:<12} | {estado_color}")
    print(border + "\n")

def listar_socios_completo():
    print(f"\n{CELESTE}--- Listado completo de socios ---{RESET}")
    mostrar_tabla_socios(lista_socios)

def buscar_socio_detalle():
    print(f"\n{CELESTE}--- Consultar detalle de un socio ---{RESET}")
    socio = obtener_socio_por_indicador("Ingrese DNI, Nombre o N° de carnet: ")
    if not socio:
        return
    
    print(f"\n{CELESTE}============ FICHA DEL SOCIO ============{RESET}")
    print(f"{NEGRITA}N° Carnet:{RESET} {socio['nro_carnet']}")
    print(f"{NEGRITA}DNI:{RESET} {socio['dni']}")
    print(f"{NEGRITA}Nombre:{RESET} {socio['nombre']}")
    print(f"{NEGRITA}Teléfono:{RESET} {socio['telefono']}")
    print(f"{NEGRITA}Email:{RESET} {socio['email']}")
    print(f"{NEGRITA}Fecha Alta:{RESET} {socio['fecha_alta']}")
    print(f"{NEGRITA}Categoría:{RESET} {socio['categoria'].capitalize()}")
    
    estado_color = f"{VERDE}Activo{RESET}" if socio['estado'] == "activo" else f"{ROJO}Dado de baja{RESET}"
    print(f"{NEGRITA}Estado:{RESET} {estado_color}")
    print(f"{CELESTE}----------------------------------------{RESET}")
    
    # Requisito extra: Ver libros prestados e historial
    print(f"{NEGRITA}Libros prestados actualmente:{RESET}")
    if socio["prestamos_actuales"]:
        for libro in socio["prestamos_actuales"]:
            print(f"  • {libro}")
    else:
        print(f"  {GRIS}Ninguno{RESET}")
        
    print(f"{NEGRITA}Historial de préstamos pasados:{RESET}")
    if socio["historial_prestamos"]:
        for libro in socio["historial_prestamos"]:
            print(f"  • {libro}")
    else:
        print(f"  {GRIS}Sin registros anteriores{RESET}")
    print(f"{CELESTE}========================================{RESET}\n")

def obtener_socio_por_indicador(mensaje):
    busqueda = leer_texto_no_vacio(mensaje).lower()
    for socio in lista_socios:
        if (busqueda.isdigit() and (socio["nro_carnet"] == int(busqueda) or socio["dni"] == busqueda)) or \
           (busqueda in socio["nombre"].lower()):
            return socio
    print(f"{ROJO}Error: No se encontró ningún socio que coincida con la búsqueda.{RESET}\n")
    return None

def leer_texto_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f"{ROJO}Error: Este campo no puede quedar vacío.{RESET}")

def registrar_socio():
    global ultimo_carnet
    print(f"\n{CELESTE}--- Registrar un nuevo socio ---{RESET}")
    dni = leer_texto_no_vacio("DNI: ")
    nombre = leer_texto_no_vacio("Nombre completo: ")
    telefono = leer_texto_no_vacio("Teléfono de contacto: ")
    
    # Manejo del email opcional (pensado para los jubilados)
    email_input = input("Email (Presione Enter si no posee): ").strip()
    email = email_input if email_input else "No posee"
    
    print("\nCategoría de socio:")
    categorias = ["general", "jubilado", "estudiante", "infantil"]
    categoria = seleccionar_opcion_lista("Seleccione la categoría (número): ", categorias)
    
    # Captura automática de la fecha actual en formato DD/MM/AAAA
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    ultimo_carnet += 1
    nuevo_socio = {
        "nro_carnet": ultimo_carnet, "dni": dni, "nombre": nombre, "telefono": telefono,
        "email": email, "fecha_alta": fecha_actual, "categoria": categoria, "estado": "activo",
        "prestamos_actuales": [], "historial_prestamos": []
    }
    lista_socios.append(nuevo_socio)
    print(f"\n{VERDE}¡Socio '{nombre}' registrado con éxito! N° de Carnet asignado: {ultimo_carnet}{RESET}\n")

def seleccionar_opcion_lista(mensaje, opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"  {AMARILLO}{i}.{RESET} {opcion}")
    while True:
        opc = leer_entero(mensaje)
        if 1 <= opc <= len(opciones):
            return opciones[opc - 1]
        print(f"{ROJO}Error: Elija una opción entre 1 y {len(opciones)}.{RESET}")

def leer_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print(f"{ROJO}Error: Por favor, ingrese un número entero válido.{RESET}")