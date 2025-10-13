from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from tareas.models import Tarea

content_type = ContentType.objects.get_for_model(Tarea)
perm_ver_mis_tareas = Permission.objects.get(
    codename='ver_mis_tareas',
    content_type=content_type
)

# Crear 3 usuarios
usuarios_datos = [
    ('ana', 'ana123'),
    ('carlos', 'carlos123'),
    ('lucia', 'lucia123'),
]

usuarios = []
for username, password in usuarios_datos:
    user = User.objects.create_user(username=username, password=password)
    user.user_permissions.add(perm_ver_mis_tareas)
    usuarios.append(user)
    print(f"Usuario creado: {username}")

tareas_ejemplo = [
    ("Tarea de Ana 1", "Descripción de la tarea de Ana", usuarios[0]),
    ("Tarea de Ana 2", "Otra tarea de Ana", usuarios[0]),
    ("Informe mensual", "Preparar informe de ventas", usuarios[1]),
    ("Reunión equipo", "Organizar reunión semanal", usuarios[1]),
    ("Lista de compras", "Comprar ingredientes", usuarios[2]),
    ("Leer libro", "Terminar capítulo 5", usuarios[2]),
]

for titulo, desc, creador in tareas_ejemplo:
    Tarea.objects.create(titulo=titulo, descripcion=desc, creador=creador)
    print(f"Tarea creada: '{titulo}' para {creador.username}")

print("\n¡Usuarios y tareas creados exitosamente!")