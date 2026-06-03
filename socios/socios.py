import os
import json
from datetime import datetime


# Colores ANSI para la consola
RESET = "\033[0m"
NEGRITA = "\033[1m"
CELESTE = "\033[1;36m"
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
GRIS = "\033[90m"

# Ruta para el almacenamiento persistente
RUTA_JSON_SOCIOS = os.path.join(os.path.dirname(__file__), "socios.json")

lista_socios = []

ultimo_carnet = max(s["nro_carnet"] for s in lista_socios) if lista_socios else 0 # 

def guardar_socios_json(): # Guarda la lista de socios en formato JSON
    try:
        with open(RUTA_JSON_SOCIOS, "w", encoding="utf-8") as f:
            json.dump(lista_socios, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"{ROJO}Error al guardar socios en archivo: {e}{RESET}")

def cargar_socios_json(): # Carga los socios desde el JSON o crea el archivo inicial si no existe
    global lista_socios, ultimo_carnet
    if not os.path.exists(RUTA_JSON_SOCIOS):
        guardar_socios_json()
        return
    try:
        with open(RUTA_JSON_SOCIOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if isinstance(datos, list):
                lista_socios = datos
                if lista_socios:
                    ultimo_carnet = max(s["nro_carnet"] for s in lista_socios)
                else:
                    ultimo_carnet = 0
    except Exception as e:
        print(f"{ROJO}Error al cargar socios desde JSON: {e}{RESET}")

# Cargar datos al importar el módulo
cargar_socios_json()

# Dibuja una tabla estilizada en la consola con la lista de socios
def mostrar_tabla_socios(socios):
    if not socios:
        print(f"\n{ROJO}No se encontraron socios para mostrar.{RESET}\n")
        return
    border = f"{CELESTE}" + "-" * 115 + f"{RESET}"
    print(border)
    print(f"{NEGRITA}{'Carnet':<8} | {'DNI':<10} | {'Nombre Completo':<25} | {'Teléfono':<15} | {'Categoría':<12} | {'Alta':<12} | {'Ult. visita':<12} | {'Estado'}{RESET}")
    print(border)
    for socio in socios:
        nombre_completo = socio["nombre"][:23] + ".." if len(socio["nombre"]) > 25 else socio["nombre"]
        estado = socio["estado"]
        estado_padded = f"{estado:<12}"
        if estado == "activo":
            estado_color = f"{VERDE}{estado_padded}{RESET}"
        else:
            estado_color = f"{ROJO}{estado_padded}{RESET}"
            
        print(f"{socio['nro_carnet']:<8} | {socio['dni']:<10} | {nombre_completo:<25} | {socio['telefono']:<15} | {socio['categoria']:<12} | {socio['fecha_alta']:<12} | {socio['ultima_visita']:<12} | {estado_color}")
    print(border + "\n")

# Imprime en pantalla el listado de todos los socios
def listar_socios_completo():
    cargar_socios_json() # Cada vez que se llame a esta funcion, se van a vovler a cargar los datos desde el json por si hubo alguna modificación.

    print(f"\n{CELESTE}--- Listado completo de socios ---{RESET}")
    mostrar_tabla_socios(lista_socios)

# Busca un socio y muestra su ficha detallada e historial de lecturas
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
    print(f"{NEGRITA}Ultima Visita:{RESET} {socio['ultima_visita']}")
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
    print(f"{CELESTE}========================================{RESET}")
    
    # Advertencia sobre socios que estan cerca de cumplir 2 años desde su ultima visita (se avisa a partir de un mes antes de la baja automatica)
    fecha_uv = datetime.strptime(socio['ultima_visita'], "%d/%m/%Y")
    dias_inactivo = (datetime.now() - fecha_uv).days
    if socio['estado'] == 'activo' and dias_inactivo >= 700:
        print(f"{AMARILLO}⚠ ADVERTENCIA: Socio inactivo por {dias_inactivo} días. Se dará de baja automáticamente al cumplir 730 días (2 años).{RESET}")
        print(f"{CELESTE}========================================{RESET}\n")

# Busca y retorna el objeto socio por DNI, nombre o carnet
def obtener_socio_por_indicador(mensaje):
    busqueda = leer_texto_no_vacio(mensaje).lower()
    for socio in lista_socios:
        if (busqueda.isdigit() and (socio["nro_carnet"] == int(busqueda) or socio["dni"] == busqueda)) or \
           (busqueda in socio["nombre"].lower()):
            return socio
    print(f"{ROJO}Error: No se encontró ningún socio que coincida con la búsqueda.{RESET}\n")
    return None

def leer_texto_no_vacio(mensaje): # Solicita y valida que la entrada de texto no sea vacía
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f"{ROJO}Error: Este campo no puede quedar vacío.{RESET}")

# Registra un nuevo socio y genera su número de carnet secuencial
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
        "email": email, "fecha_alta": fecha_actual, "ultima_visita": fecha_actual,"categoria": categoria, "estado": "activo",
        "prestamos_actuales": [], "historial_prestamos": []
    }
    lista_socios.append(nuevo_socio)
    guardar_socios_json()
    print(f"\n{VERDE}¡Socio '{nombre}' registrado con éxito! N° de Carnet asignado: {ultimo_carnet}{RESET}\n")

def seleccionar_opcion_lista(mensaje, opciones): # Muestra y valida una selección numérica de una lista de opciones
    for i, opcion in enumerate(opciones, 1):
        print(f"  {AMARILLO}{i}.{RESET} {opcion}")
    while True:
        opc = leer_entero(mensaje)
        if 1 <= opc <= len(opciones):
            return opciones[opc - 1]
        print(f"{ROJO}Error: Elija una opción entre 1 y {len(opciones)}.{RESET}")

def leer_entero(mensaje): # Solicita y valida que el valor ingresado sea un número entero
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print(f"{ROJO}Error: Por favor, ingrese un número entero válido.{RESET}")

def actualizar_datos_contacto(): # Modifica el teléfono o el email de un socio existente
    print(f"\n{CELESTE}--- Actualizar datos de contacto ---{RESET}")
    socio = obtener_socio_por_indicador("Ingrese DNI, Nombre o N° de carnet del socio: ")
    if not socio:
        return
    
    print(f"\nModificando datos de: {NEGRITA}{socio['nombre']}{RESET}")
    print(f"Teléfono actual: {socio['telefono']}")
    nuevo_tel = input("Nuevo teléfono (Presione Enter para mantener el actual): ").strip()
    if nuevo_tel:
        socio["telefono"] = nuevo_tel
        
    print(f"Email actual: {socio['email']}")
    nuevo_email = input("Nuevo email (Presione Enter para mantener el actual / espacio para borrarlo): ")
    if nuevo_email:
        socio["email"] = "No posee" if nuevo_email.isspace() else nuevo_email.strip()
        
    guardar_socios_json()
    print(f"\n{VERDE}¡Datos de contacto actualizados con éxito!{RESET}\n")

def dar_de_baja_socio(): # Realiza la baja lógica de un socio cambiando su estado a inactivo
    print(f"\n{CELESTE}--- Dar de baja un socio ---{RESET}")
    socio = obtener_socio_por_indicador("Ingrese DNI, Nombre o N° de carnet del socio a dar de baja: ")
    if not socio:
        return
        
    if socio["estado"] == "dado de baja":
        print(f"{ROJO}El socio ya se encuentra dado de baja.{RESET}\n")
        return
        
    print(f"\nSocio seleccionado: {NEGRITA}'{socio['nombre']}'{RESET} (Categoría: {socio['categoria']})")
    print(f"{AMARILLO}Motivo sugerido: Solicitud personal o inactividad mayor a 2 años.{RESET}")
    confirmar = input(f"{ROJO}¿Está seguro de que desea dar de baja a este socio? (s/n): {RESET}").strip().lower()
    if confirmar == 's':
        socio["estado"] = "dado de baja"
        guardar_socios_json()
        print(f"{VERDE}¡Socio dado de baja con éxito!{RESET}\n")
    else:
        print(f"Operación cancelada.\n")

def revisar_y_aplicar_bajas_automaticamente(): # Se verifica los socios inactivos por más de 2 años y se da de baja automáticamente
    global lista_socios
    fecha_hoy = datetime.now()
    bajas_realizadas = []
    
    for socio in lista_socios:
        if socio["estado"] == "activo":
            try:
                fecha_ultima_visita = datetime.strptime(socio["ultima_visita"], "%d/%m/%Y")
                dias_inactivo = (fecha_hoy - fecha_ultima_visita).days
                
                if dias_inactivo >= 730:  # 2 años o más
                    socio["estado"] = "dado de baja"
                    bajas_realizadas.append({
                        "nombre": socio["nombre"],
                        "carnet": socio["nro_carnet"],
                        "dias_inactivo": dias_inactivo
                    })
            except Exception as e:
                print(f"{ROJO}Error al procesar fecha de {socio['nombre']}: {e}{RESET}")
    
    if bajas_realizadas:
        guardar_socios_json()
        print(f"\n{AMARILLO}--- BAJAS AUTOMÁTICAS POR INACTIVIDAD ---{RESET}")
        for baja in bajas_realizadas:
            print(f"{AMARILLO}  • {baja['nombre']} (Carnet N°{baja['carnet']}) - Inactivo {baja['dias_inactivo']} días{RESET}")
        print(f"{VERDE}Se dieron de baja {len(bajas_realizadas)} socio(s) automáticamente.{RESET}\n")

def limpiar_pantalla(): # Limpia la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_socios(): # Muestra las opciones del menú de socios
    limpiar_pantalla()
    cargar_socios_json() # Cada vez que se llame a esta funcion, se van a vovler a cargar los datos desde el json por si hubo alguna modificación.
    revisar_y_aplicar_bajas_automaticamente() # Se verifica los socios inactivos por más de 2 años y se da de baja automáticamente
    
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

def menu_principal_socios(): # Bucle de control del menú de socios
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
            actualizar_datos_contacto()
        elif opcion == "5":
            dar_de_baja_socio()
        else:
            print(f"\n{ROJO}Opción inválida.{RESET}")

        input(f"\n{GRIS}Presione Enter para continuar...{RESET}")