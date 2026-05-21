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

Por ahora, implementamos la primera etapa (el **Catálogo de Libros**), que te permite:
- **Cargar libros nuevos**: Registra título, autor, género, año y procedencia (si fue comprado o quién lo donó). El ID de inventario se genera solo de forma secuencial.
- **Listar el catálogo**: Se armó una tabla en la consola bien formateada que acomoda los anchos y resalta el estado del libro (Disponible en verde, Prestado en amarillo, En reparación en celeste, Dado de baja en rojo).
- **Buscar libros**: Podés meter un ID, parte del título o el autor y te trae las coincidencias sin importar mayúsculas/minúsculas.
- **Filtrar**: Para ver rápido qué libros están prestados o cuáles se mandaron a encuadernar.
- **Modificar estado / Dar de baja**: Para cuando un libro vuelve, se rompe, o lamentablemente se pierde (con cartel de confirmación para no meter la pata).
- **Eliminar por completo**: Si cargaste algo mal por error, podés borrar el registro usando una doble confirmación escribiendo `ELIMINAR`.

---

## 📐 Pautas de diseño del TP que seguimos:
Para cumplir con los requisitos que nos pidieron en la cátedra:
- **Funciones cortas**: Ninguna función del código pasa las 30 líneas de código (las modularizamos y dividimos las de lógica de las que solo imprimen menús).
- **Estructuras nativas**: Toda la información se maneja con estructuras de Python:
  - Los datos de cada libro están metidos en un `dict`.
  - La colección completa de libros es una `list` de diccionarios.
  - Para los menús y listados fijos usamos `tuple`.
- **Validaciones**: El sistema no se rompe si ponés mal una opción o ingresás texto donde va un número (como el año). Te avisa y te vuelve a preguntar.
- **Estética retro pero cuidada**: Usamos códigos de colores ANSI y caracteres de bordes dobles (`║`, `═`, `╔`) para que el menú de consola no sea una pared de texto plano aburrida y se entienda al toque.
