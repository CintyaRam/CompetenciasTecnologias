# 📋 Gestor de Tareas — Documentación

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

## 🗃️ Estructura del Proyecto


| Archivo/Carpeta | Descripción |
|------------------|-------------|
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

## ⚙️ Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

git clone https://github.com/CintyaRam/EvaluacionModulo6Django.git
cd gestor-tareas


---


### 2. Crear y activar el entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```
---


### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
---


### 4. Crear superusuario (opcional, para login)
```bash
python manage.py createsuperuser
python manage.py migrate
```

---

### 5. Iniciar el servidor
```bash
python manage.py runserver
```
---

✅ **Abre tu navegador en:** [http://127.0.0.1:8000](http://127.0.0.1:8000)  
👉 Al entrar, serás redirigido automáticamente a `/tareas/`.

---

### 🔐 Seguridad y Notas

- **No se usan migraciones** para el modelo `Tarea`.
- **Todas las tareas están en memoria**: no se guardan en la base de datos.
- **Solo usuarios autenticados** pueden acceder a las funcionalidades.
- **No hay persistencia**: al reiniciar el servidor, se pierden todas las tareas.

---

### 🛠️ Tecnologías Usadas

- Python 3.10+
- Django 5.2
- Bootstrap