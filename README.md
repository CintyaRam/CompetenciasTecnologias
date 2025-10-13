# 🏆 Competencias Tecnológicas

Este repositorio tiene como objetivo mostrar soluciones a **ejercicios, desafíos y competencias técnicas** resueltos en diferentes **lenguajes de programación**.  

---

## 🧩 ¿Qué encontrarás aquí?

Cada carpeta representa un desafío o competencia resuelta, con su solución en uno o más lenguajes.  
Este repositorio evolucionará incluyendo distintas tecnologías y enfoques.

### 🐍 Lenguajes actuales:
- **Python** (Problemas iniciales, algoritmos básicos, POO y proyectos funcionales)
- **SQL / MySQL** (Modelado, normalización, DDL, DML, procedimientos almacenados, consultas complejas)
- **Django** (Aplicación funcional con vistas, formularios, autenticación y manejo de sesiones en memoria; sin base de datos persistente. Incluye uso de **Bootstrap**, **plantillas HTML** y **autenticación de usuarios** mediante el sistema integrado de Django)
---

## 🗂️ Estructura del repositorio

| Archivo/Carpeta | Descripción |
|------------------|-------------|
| **Competencias_python/**  | Carpeta con pequeños proyectos funcionales para mostrar competencias en Python |
| ├── `bucle_for_basico1.py`   | Recorridos básicos usando bucles `for` |
| ├── `calculadora_pythonirica.py` | Calculadora con distintos tipos de datos y operaciones, incluye sentencias condicionales |
| ├── `condicionales.py` | Uso de sentencias condicionales (`if`, `elif`, `else`) |
| ├── `estructuras_datos.py`  | Demostración del uso de estructuras: listas, tuplas, diccionarios y sets |
| ├── `evaluacion_del_modulo.py`  | Integración de todos los fundamentos de programación en Python |
| ├── `funciones_intermedias_1.py`     | Declaración y uso de funciones, variables locales y sintaxis |
| ├── `probando_python.py`      | Prueba de funciones y sentencias condicionales para entender el comportamiento en consola |
| **Sistema_gestion_biblioteca/** | Proyecto completo de gestión bibliotecaria con Programación Orientada a Objetos (POO) |
| ├── `main.py` | Punto de entrada del sistema |
| ├── `Libro.py` | Clase base: encapsulamiento, métodos especiales y persistencia |
| ├── `LibroDigital.py` | Subclase que hereda de `Libro` (demostración de herencia y polimorfismo) |
| ├── `Biblioteca.py` | Gestor principal con menú interactivo y persistencia en archivo |
| ├── `biblioteca.txt` | Archivo de datos en formato CSV |
| ├── `README.md` | Documentación detallada del proyecto |
| **sql/** | Proyecto de Sistema de Inventario - Star Wars Edition (Gestión de Bases de Datos Relacionales) |
| ├── `inventario_bbdd_portafolio.sql` | Script SQL completo: DDL, DML, procedimientos, consultas, comentarios educativos |
| ├── `ERD_inventario_portafolio.mwb` | Modelo ER en formato MySQL Workbench (editable) |
| ├── `ERD_imagen_inventario_portafolio.png` | Diagrama Entidad-Relación (visualización rápida) |
| **GESTOR_TAREAS/** | Proyecto Django de gestión de tareas con estructura modular |
| ├── **gestor_tareas/** | Configuración principal del proyecto |
| │   ├── `__init__.py` | Inicialización del módulo del proyecto |
| │   ├── `asgi.py` | Configuración para el servidor ASGI |
| │   ├── `settings.py` | Configuración general del proyecto (apps, BD, rutas estáticas, etc.) |
| │   ├── `urls.py` | Enrutamiento global del proyecto |
| │   └── `wsgi.py` | Configuración para el servidor WSGI |
| ├── **static/** | Archivos estáticos (CSS, imágenes, etc.) |
| │   ├── `css/` | Hojas de estilo del proyecto |
| │   └── `img/` | Imágenes utilizadas en las plantillas |
| ├── **tareas/** | Aplicación principal del proyecto |
| │   ├── `__init__.py` | Inicialización del módulo de la app |
| │   ├── `admin.py` | Registro de modelos para el panel de administración |
| │   ├── `apps.py` | Configuración de la aplicación Django |
| │   ├── `formularios.py` | Formularios personalizados para manejo de tareas |
| │   ├── `models.py` | Modelo de datos `Tarea` (definido pero no conectado a la BD) |
| │   ├── `tests.py` | Pruebas automáticas del módulo |
| │   ├── `urls.py` | Rutas específicas de la app `tareas` |
| │   ├── `views.py` | Lógica de control y renderizado de vistas |
| │   └── **templates/** | Plantillas HTML del proyecto |
| │       ├── `base.html` | Plantilla base reutilizable |
| │       ├── `crear_tarea.html` | Formulario para crear nuevas tareas |
| │       ├── `detalles_tarea.html` | Vista con detalles individuales de una tarea |
| │       ├── `eliminar_tareas.html` | Confirmación y eliminación de tareas |
| │       └── `home.html` | Página principal con listado de tareas |
| ├── **venv/** | Entorno virtual del proyecto (auto-generado) |
| ├── `.gitignore` | Archivos y carpetas ignorados por Git |
| ├── `db.sqlite3` | Base de datos SQLite (vacía, sin uso activo) |
| ├── `manage.py` | Script principal de administración de Django |
| ├── `README.md` | Archivo de documentación del proyecto |
| ├── `requirements.txt` | Dependencias del proyecto |
| └── `shell.py` | Script opcional (puede eliminarse si no se usa) |


---

## 🚀 Sistema de Gestión Bibliotecaria

Proyecto desarrollado con **Programación Orientada a Objetos (POO)** que simula un sistema completo de biblioteca. Incluye:

- ✅ **Encapsulamiento**: atributo privado `__estado` con métodos `get` y `set`.
- ✅ **Herencia y polimorfismo**: clase `LibroDigital` que extiende `Libro`.
- ✅ **Persistencia**: datos guardados en `biblioteca.txt` (formato CSV).
- ✅ **Menú interactivo**: opciones para agregar, eliminar, buscar, prestar y devolver libros.
- ✅ **Manejo de errores**: validación de entradas y gestión robusta de archivos.

> 📌 Este proyecto demuestra el uso avanzado de POO en Python, ideal para consolidar conocimientos de clases, métodos, archivos y diseño modular.

## 🗃️ Sistema de Inventario - Star Wars Edition (Gestión de Bases de Datos)

Proyecto académico y profesional desarrollado para demostrar competencias en gestión de bases de datos relacionales, usando **MySQL**. Incluye:

- ✅ **Modelado ER**: Diagrama generado con MySQL Workbench (archivo .mwb editable y .png para visualización).
- ✅ **Normalización hasta 3NF**: Tablas diseñadas sin redundancias, con claves primarias y foráneas.
- ✅ **DDL (Data Definition Language)**: Creación de esquema, tablas, índices, restricciones.
- ✅ **DML (Data Manipulation Language)**: Inserción, actualización (vía procedimiento), eliminación (ejemplo comentado).
- ✅ **Procedimiento Almacenado**: RegistrarTransaccion con manejo transaccional (START TRANSACTION, COMMIT, ROLLBACK), validación de stock y copia de precios históricos.
- ✅ **Consultas SQL Complejas**: Uso de JOIN, GROUP BY, funciones de agregación, subconsultas.
- ✅ **Datos de prueba temáticos**: Proveedores y productos del universo Star Wars.
- ✅ **Documentación interna**: Todo el script está comentado para uso educativo y evaluación de portafolio.

> 📌 Este proyecto cumple con las siguientes competencias en gestión de bases de datos: modelado, normalización, DDL, DML, consultas, procedimientos y transacciones.

---

# 📋 Gestor de Tareas - Liz-Taylor

Una aplicación simple para gestionar tareas personales, desarrollada con **Django 5.2**.  
Este proyecto **no utiliza base de datos**: todas las tareas se almacenan en memoria (en la sesión del usuario), ideal para demostraciones o aprendizaje.

---

## 🌟 Funcionalidades

- ✅ **Crear tareas** con título y descripción.  
- ✅ **Ver solo tus tareas** (filtradas por usuario autenticado).  
- ✅ **Ver detalles** de una tarea específica.  
- ✅ **Eliminar tareas** individualmente.  
- ✅ **Autenticación básica** (login/logout con usuarios del sistema).  

> 💡 **Importante**: los datos son temporales. Se pierden al reiniciar el servidor.

---

## ❤️ ¿Te gustó este proyecto?

- ¡Sigue mi perfil para ver más proyectos como este!

---
