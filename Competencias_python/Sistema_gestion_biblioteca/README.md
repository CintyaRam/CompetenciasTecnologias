# 📚 Sistema de Gestión Bibliotecaria

> Un sistema de consola desarrollado en **Python con Programación Orientada a Objetos (POO)** que permite gestionar una biblioteca de libros. Incluye persistencia en archivo, encapsulamiento, herencia y polimorfismo.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)

---

## 🎯 Funcionalidades

- ✅ Agregar libros
- ✅ Eliminar libros
- ✅ Listar todos los libros
- ✅ Buscar por título
- ✅ Prestar y devolver libros
- ✅ Persistencia en archivo (`biblioteca.txt`)
- ✅ Manejo de errores robusto

---

## 🧱 Arquitectura del Sistema

### 1. `Libro` – Clase Base

- Representa un libro con los siguientes atributos:
  - `titulo`: str
  - `autor`: str
  - `anio_publicacion`: int
  - `__estado`: str (privado, solo accesible mediante métodos)
- Métodos:
  - `__init__(titulo, autor, anio_publicacion, estado)` → constructor
  - `get_estado()` → devuelve el estado actual
  - `set_estado(nuevo_estado)` → cambia el estado
  - `__str__()` → retorna representación legible del libro
  - `to_csv()` → convierte el libro a formato CSV: `"titulo,autor,año,estado"`
  - `from_csv(linea)` → crea una instancia desde una línea de texto
- El estado solo puede ser `"Disponible"` o `"Prestado"`
- El uso de `__estado` garantiza encapsulamiento

### 2. `LibroDigital` – Subclase (Demostración de POO)

- Hereda de la clase `Libro`
- Atributo adicional:
  - `formato`: str (ej: "PDF", "EPUB")
- Métodos:
  - `__init__(titulo, autor, anio_publicacion, estado, formato)` → llama a `super()`
  - `__str__()` → extiende la representación del libro base
- No se almacena en el archivo `biblioteca.txt`
- Se incluye únicamente como ejemplo de:
  - Herencia
  - Polimorfismo
- No forma parte del flujo principal del sistema

### 3. `Biblioteca` – Gestor Principal

- Controla la gestión de todos los libros
- Atributo:
  - `lista_libros`: list → almacena instancias de `Libro` (y `LibroDigital` si se crean)
- Métodos:
  - `__init__()` → carga los libros desde `biblioteca.txt`
  - `agregar_libro()` → permite ingresar un nuevo libro y guardarlo en el archivo
  - `eliminar_libro()` → busca por título y lo elimina (actualiza el archivo)
  - `listar_libros()` → muestra todos los libros en pantalla
  - `buscar_libro()` → busca por título y permite cambiar el estado
  - `prestar_libro()` → cambia el estado a `"Prestado"`
  - `devolver_libro()` → cambia el estado a `"Disponible"`
  - `sobreescribir_archivo()` → guarda toda la lista en el archivo
  - `menu()` → menú interactivo con opciones del 1 al 7
- Todos los accesos al archivo usan manejo de excepciones

### 4. Formato del Archivo `biblioteca.txt`

- Almacena los libros en formato CSV
- Cada línea sigue el formato:
  - `"titulo,autor,año,estado"`
- Ejemplo:
  - `El Libro De La Selva,Rudyard Kipling,1894,Disponible`
  - `El Principito,Antoine De Saint-Exupéry,1943,Prestado`
- Se usa `split(",", 3)` para permitir comas en títulos o nombres
- El archivo se carga al iniciar y se actualiza tras cada modificación
- Si no existe, se muestra un mensaje; se crea al agregar el primer libro

### 5. Cómo Ejecutar el Proyecto

- Requisitos:
  - Python 3 instalado
  - Todos los archivos en la misma carpeta
- Archivos necesarios:
  - `Libro.py`
  - `LibroDigital.py`
  - `Biblioteca.py`
  - `main.py` → punto de entrada
  - `biblioteca.txt` → opcional (se crea al agregar libros)
- Pasos:
  - Abrir terminal en la carpeta del proyecto
  - Ejecutar:
    - `python main.py`
- El sistema carga los libros y muestra el menú principal

### 6. Encapsulamiento

- El estado del libro está protegido como atributo privado (`__estado`)
- Se respeta el principio de encapsulamiento de la POO

### 7. Estructura del Proyecto

- Archivos principales:
  - `main.py` → inicia el programa
  - `Libro.py` → define la clase base
  - `LibroDigital.py` → subclase con herencia
  - `Biblioteca.py` → gestor y menú
  - `biblioteca.txt` → almacenamiento persistente
  - `Diagrama de clases_evaluacion.png` → diagrama de clases del sistema
  - `README.md` → documentación
- Todas las clases están correctamente separadas
- El código es modular, limpio y fácil de extender

### 8. Créditos y Licencia

- Proyecto desarrollado por: **Cintya Ramírez**
- Para fines educativos y demostración de POO en Python