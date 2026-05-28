# Trabajo Integrador: Sistema de Gestión de Biblioteca - "El Aljibe"

Este es el proyecto integrador para la materia Programación 1. Desarrollamos un sistema de consola en Python para digitalizar el registro manual de la **Biblioteca Popular "El Aljibe"** (un pueblo de Entre Ríos). La idea principal es reemplazar el cuaderno de préstamos gigante que usan las voluntarias por una herramienta simple y directa.

## 🚀 Cómo ponerlo a correr
No necesitás instalar bases de datos ni dependencias externas complejas. Solo clonás el repo y ejecutás en tu terminal:

```bash
python menuPrincipal.py
```

*Nota: Requiere Python 3.10 o superior (usamos `match-case` para los menús).*

---

## 🛠️ ¿Qué tiene el sistema actualmente?

Ya tenemos implementadas las dos primeras grandes etapas del sistema:

### 📚 1. Catálogo de Libros
Te permite gestionar todo el inventario físico de la biblioteca:
- **Cargar libros nuevos**: Registra título, autor, género, año y procedencia (si fue comprado o quién lo donó). El ID de inventario se genera de forma secuencial.
- **Listar el catálogo**: Se armó una tabla en la consola bien formateada que acomoda los anchos y resalta el estado del libro (Disponible en verde, Prestado en amarillo, En reparación en celeste, Dado de baja en rojo).
- **Buscar libros**: Podés meter un ID, parte del título o el autor y te trae las coincidencias sin importar mayúsculas/minúsculas.
- **Filtrar**: Para ver rápido qué libros están prestados o cuáles se mandaron a encuadernar.
- **Modificar estado / Dar de baja**: Para cuando un libro vuelve, se rompe, o lamentablemente se pierde (con cartel de confirmación para no meter la pata).
- **Eliminar por completo**: Si cargaste algo mal por error, podés borrar el registro usando una doble confirmación escribiendo `ELIMINAR`.

### 👥 2. Gestión de Socios
Diseñado a medida para la gente del pueblo (pensando en que no todos se manejan igual con la tecnología):
- **Registrar socio nuevo**: Guarda DNI, nombre, teléfono y categoría (General, Jubilado, Estudiante o Infantil). Captura la fecha de alta automáticamente.
- **Manejo de email opcional**: Pensado especialmente para los socios jubilados que tal vez no tienen correo; el sistema les asigna "No posee" y te deja seguir sin problemas.
- **Listado completo**: Una tabla limpia que muestra los datos de contacto y si el socio está Activo (verde) o Inactivo/Baja (rojo).
- **Ficha de socio detallada**: Al buscar un socio por nombre, DNI o N° de carnet, te dibuja una ficha completa con sus datos y un historial detallado de los libros que tiene prestados ahora y los que ya devolvió en el pasado.
- **Actualizar datos**: Si un socio cambia de celular o quiere agregar su mail, se le modifican los datos de contacto al toque sin alterar su fecha de alta o N° de carnet.
- **Baja lógica**: Los socios no se eliminan del todo para no perder su historial de lectura; simplemente cambian su estado a "dado de baja".

---

## 📐 Pautas de diseño del TP que seguimos:
Para cumplir con los requisitos que nos pidieron en la cátedra:
- **Estructura modular limpia**: Separamos el proyecto en subcarpetas lógicas (`catalogoDeLibros/`, `socios/`) con sus propios módulos independientes para que sea súper fácil de leer y mantener.
- **Funciones cortas y comentadas**: Ninguna función del código pasa las 30 líneas de código (las modularizamos y dividimos las de lógica de las que solo imprimen menús). Además, todas las funciones principales tienen un comentario corto y al pie al lado de su definición explicando exactamente qué hacen.
- **Estructuras nativas**: Toda la información se maneja con estructuras de Python:
  - Los datos de cada libro y cada socio están metidos en un `dict`.
  - La colección completa de libros y socios son objetos `list` de diccionarios.
  - Para los menús y listados fijos usamos `tuple`.
- **Validaciones**: El sistema no se rompe si ponés mal una opción o ingresás texto donde va un número (como el año o el DNI). Te avisa y te vuelve a preguntar.
- **Estética retro pero cuidada**: Usamos códigos de colores ANSI y caracteres de bordes dobles (`║`, `═`, `╔`) para que el menú de consola no sea una pared de texto plano aburrida y se entienda al toque.
- **Repositorio ordenado**: Configuramos el `.gitignore` para obviar automáticamente archivos temporales de Python, carpetas de IDEs (`.vscode`, `.idea`) y todos los PDF con apuntes de la cátedra que guardamos en la carpeta `catedra/`, para subir al repo solo código limpio del proyecto.
