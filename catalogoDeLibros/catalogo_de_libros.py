import os
import json

# Colores ANSI para la consola
RESET = "\033[0m"
NEGRITA = "\033[1m"
CELESTE = "\033[1;36m"
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
GRIS = "\033[90m"

# Ruta para el almacenamiento persistente
RUTA_JSON_LIBROS = os.path.join(os.path.dirname(__file__), "libros.json")

# Inicialización de datos semilla
lista_libros = [
    {
        "id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez",
        "genero": "novela", "anio_publicacion": 1967, "estado": "disponible",
        "procedencia": "donado por escuela N°4"
    },
    {
        "id": 2, "titulo": "El Aleph", "autor": "Jorge Luis Borges",
        "genero": "cuento", "anio_publicacion": 1949, "estado": "disponible",
        "procedencia": "comprado"
    },
    {
        "id": 3, "titulo": "Rayuela", "autor": "Julio Cortázar",
        "genero": "novela", "anio_publicacion": 1963, "estado": "prestado",
        "procedencia": "donado por Elsa Morales"
    }
]

ultimo_id_libro = 3

def guardar_libros_json(): # Guarda la lista de libros en formato JSON
    try:
        with open(RUTA_JSON_LIBROS, "w", encoding="utf-8") as f:
            json.dump(lista_libros, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"{ROJO}Error al guardar libros en archivo: {e}{RESET}")

def cargar_libros_json(): # Carga los libros desde el JSON o crea el archivo inicial si no existe
    global lista_libros, ultimo_id_libro
    if not os.path.exists(RUTA_JSON_LIBROS):
        guardar_libros_json()
        return
    try:
        with open(RUTA_JSON_LIBROS, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if isinstance(datos, list):
                lista_libros = datos
                if lista_libros:
                    ultimo_id_libro = max(l["id"] for l in lista_libros)
                else:
                    ultimo_id_libro = 0
    except Exception as e:
        print(f"{ROJO}Error al cargar libros desde JSON: {e}{RESET}")

# Cargar datos al importar el módulo
cargar_libros_json()


def limpiar_pantalla(): # Limpia la terminal según el sistema operativo (Windows o Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_entero(mensaje): # Pide un número entero al usuario y valida que sea correcto
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print(f"{ROJO}Error: Por favor, ingrese un número entero válido.{RESET}")

def leer_texto_no_vacio(mensaje): # Pide un texto al usuario y valida que no esté vacío
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f"{ROJO}Error: Este campo no puede quedar vacío.{RESET}")

def seleccionar_opcion_lista(mensaje, opciones): # Muestra una lista de opciones y valida la selección del usuario
    for i, opcion in enumerate(opciones, 1):
        print(f"  {AMARILLO}{i}.{RESET} {opcion}")
    while True:
        opc = leer_entero(mensaje)
        if 1 <= opc <= len(opciones):
            return opciones[opc - 1]
        print(f"{ROJO}Error: Elija una opción entre 1 y {len(opciones)}.{RESET}")

def mostrar_tabla_libros(libros): # Muestra los libros en una tabla con diseño y colores por estado
    if not libros:
        print(f"\n{ROJO}No se encontraron libros para mostrar.{RESET}\n")
        return
    border = f"{CELESTE}" + "-" * 115 + f"{RESET}"
    print(border)
    print(f"{NEGRITA}{'ID':<5} | {'Título':<30} | {'Autor':<25} | {'Género':<12} | {'Año':<6} | {'Estado':<13} | {'Procedencia'}{RESET}")
    print(border)
    for l in libros:
        t_c = l["titulo"][:28] + ".." if len(l["titulo"]) > 30 else l["titulo"]
        a_c = l["autor"][:23] + ".." if len(l["autor"]) > 25 else l["autor"]
        est = l["estado"]
        estado_padded = f"{est:<13}"
        if est == "disponible":
            est_col = f"{VERDE}{estado_padded}{RESET}"
        elif est == "prestado":
            est_col = f"{AMARILLO}{estado_padded}{RESET}"
        elif est == "en reparación":
            est_col = f"{CELESTE}{estado_padded}{RESET}"
        else:
            est_col = f"{ROJO}{estado_padded}{RESET}"
        print(f"{l['id']:<5} | {t_c:<30} | {a_c:<25} | {l['genero']:<12} | {l['anio_publicacion']:<6} | {est_col} | {l['procedencia']}")
    print(border + "\n")

def cargar_libro(): # Registra un nuevo libro en el sistema pidiendo sus datos
    global ultimo_id_libro
    print(f"\n{CELESTE}--- Cargar un nuevo libro ---{RESET}")
    titulo = leer_texto_no_vacio("Título: ")
    autor = leer_texto_no_vacio("Autor: ")
    print("\nGénero:")
    generos = ["novela", "cuento", "ensayo", "infantil", "técnico", "otro"]
    genero = seleccionar_opcion_lista("Seleccione el género (número): ", generos)
    anio = leer_entero("Año de publicación: ")
    print("\nProcedencia:")
    proc_op = seleccionar_opcion_lista("Seleccione procedencia (número): ", ["Comprado", "Donado"])
    procedencia = "comprado" if proc_op == "Comprado" else f"donado por {leer_texto_no_vacio('¿Donado por quién?: ')}"
    
    ultimo_id_libro += 1
    nuevo_libro = {
        "id": ultimo_id_libro, "titulo": titulo, "autor": autor, "genero": genero,
        "anio_publicacion": anio, "estado": "disponible", "procedencia": procedencia
    }
    lista_libros.append(nuevo_libro)
    guardar_libros_json()
    print(f"\n{VERDE}¡Libro '{titulo}' cargado con éxito! ID asignado: {ultimo_id_libro}{RESET}\n")

def listar_libros_completo(): # Muestra la lista de todos los libros del catálogo
    print(f"\n{CELESTE}--- Catálogo completo de libros ---{RESET}")
    mostrar_tabla_libros(lista_libros)

def filtrar_libros_por_estado(): # Filtra y muestra los libros según el estado seleccionado
    print(f"\n{CELESTE}Filtrar por estado:{RESET}")
    estados = ["disponible", "prestado", "en reparación", "dado de baja"]
    estado_filtro = seleccionar_opcion_lista("Seleccione el estado (número): ", estados)
    libros_filtrados = [l for l in lista_libros if l["estado"] == estado_filtro]
    print(f"\n{CELESTE}--- Libros con estado '{estado_filtro}' ---{RESET}")
    mostrar_tabla_libros(libros_filtrados)

def buscar_libro(): # Busca libros por ID, título o autor (búsqueda parcial e insensible)
    print(f"\n{CELESTE}--- Buscar libro ---{RESET}")
    busq = leer_texto_no_vacio("Ingrese título, autor o número de inventario (ID): ").lower()
    resultados = []
    for l in lista_libros:
        if (busq.isdigit() and l["id"] == int(busq)) or \
           (busq in l["titulo"].lower()) or \
           (busq in l["autor"].lower()):
            resultados.append(l)
    print(f"\n{CELESTE}--- Resultados de la búsqueda: '{busq}' ---{RESET}")
    mostrar_tabla_libros(resultados)

def obtener_libro_por_id(mensaje): # Busca y retorna un libro por su ID; retorna None si no existe
    id_buscado = leer_entero(mensaje)
    for l in lista_libros:
        if l["id"] == id_buscado:
            return l
    print(f"{ROJO}Error: No se encontró ningún libro con el ID {id_buscado}.{RESET}\n")
    return None

def cambiar_estado_libro(): # Permite modificar el estado de disponibilidad o conservación de un libro
    print(f"\n{CELESTE}--- Cambiar estado de libro ---{RESET}")
    libro = obtener_libro_por_id("Ingrese el ID del libro a modificar: ")
    if not libro:
        return
    print(f"\nLibro seleccionado: {NEGRITA}'{libro['titulo']}'{RESET} (Estado actual: {libro['estado']})")
    estados = ["disponible", "prestado", "en reparación", "dado de baja"]
    nuevo_estado = seleccionar_opcion_lista("Seleccione el nuevo estado (número): ", estados)
    
    confirmar = input(f"¿Confirmar cambio a '{nuevo_estado}'? (s/n): ").strip().lower()
    if confirmar == 's':
        libro["estado"] = nuevo_estado
        guardar_libros_json()
        print(f"{VERDE}¡Estado actualizado con éxito!{RESET}\n")
    else:
        print(f"{AMARILLO}Cambio cancelado.{RESET}\n")

def dar_de_baja_libro(): # Cambia el estado de un libro a 'dado de baja' (baja lógica)
    print(f"\n{CELESTE}--- Dar de baja un libro ---{RESET}")
    libro = obtener_libro_por_id("Ingrese el ID del libro a dar de baja: ")
    if not libro:
        return
    if libro["estado"] == "dado de baja":
        print(f"{ROJO}El libro ya se encuentra dado de baja.{RESET}\n")
        return
    print(f"\nLibro seleccionado: {NEGRITA}'{libro['titulo']}'{RESET} de {libro['autor']}")
    confirmar = input(f"{ROJO}¿Está seguro de que desea dar de baja este libro? (s/n): {RESET}").strip().lower()
    if confirmar == 's':
        libro["estado"] = "dado de baja"
        guardar_libros_json()
        print(f"{VERDE}¡Libro dado de baja con éxito!{RESET}\n")
    else:
        print(f"{AMARILLO}Operación cancelada.{RESET}\n")

def eliminar_libro(): # Borra permanentemente un libro de la lista con doble confirmación
    print(f"\n{CELESTE}--- Eliminar un libro permanentemente ---{RESET}")
    libro = obtener_libro_por_id("Ingrese el ID del libro a eliminar: ")
    if not libro:
        return
    print(f"\nLibro seleccionado: {NEGRITA}'{libro['titulo']}'{RESET} de {libro['autor']}")
    print(f"{ROJO}ADVERTENCIA: Esta acción eliminará el registro permanentemente.{RESET}")
    confirmar = input("¿Está seguro de que desea eliminar este libro? (s/n): ").strip().lower()
    if confirmar == 's':
        confirmar_doble = input(f"¿REALMENTE seguro? Ingrese {ROJO}'ELIMINAR'{RESET} para confirmar: ").strip()
        if confirmar_doble == "ELIMINAR":
            lista_libros.remove(libro)
            guardar_libros_json()
            print(f"{VERDE}¡Registro eliminado permanentemente del sistema!{RESET}\n")
            return
    print(f"{AMARILLO}Eliminación cancelada.{RESET}\n")

def mostrar_menu_libros(): # Imprime en pantalla el diseño del menú del catálogo
    limpiar_pantalla()
    print(f"{CELESTE}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CELESTE}║{RESET}  {NEGRITA}CATÁLOGO DE LIBROS — Biblioteca Popular El Aljibe {RESET}{CELESTE}                ║{RESET}")
    print(f"{CELESTE}╠════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}1.{RESET} Catálogo completo de libros                                   {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}2.{RESET} Buscar libro                                                  {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}3.{RESET} Filtrar por estado                                            {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}4.{RESET} Cargar un libro                                               {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}5.{RESET} Cambiar estado de libro                                       {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}6.{RESET} Dar de baja un libro                                          {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}7.{RESET} Eliminar un libro permanentemente                             {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}   {AMARILLO}9.{RESET} Volver al menú principal                                      {CELESTE}║{RESET}")
    print(f"{CELESTE}║{RESET}                                                                    {CELESTE}║{RESET}")
    print(f"{CELESTE}╚════════════════════════════════════════════════════════════════════╝{RESET}")

def menu_principal_libros(): # Bucle principal que gestiona la navegación e interacción del menú
    while True:
        mostrar_menu_libros()
        opc = input(f"\n{AMARILLO}¿Qué querés hacer? (1-7, 9): {RESET}").strip()
        if opc == "9":
            break
        elif opc == "1":
            listar_libros_completo()
        elif opc == "2":
            buscar_libro()
        elif opc == "3":
            filtrar_libros_por_estado()
        elif opc == "4":
            cargar_libro()
        elif opc == "5":
            cambiar_estado_libro()
        elif opc == "6":
            dar_de_baja_libro()
        elif opc == "7":
            eliminar_libro()
        else:
            print(f"\n{ROJO}Opción inválida.{RESET}")
        input(f"\n{GRIS}Presione Enter para continuar...{RESET}")