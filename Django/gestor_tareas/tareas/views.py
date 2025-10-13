from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tarea
from .formularios import FormularioTareas
from django.contrib.auth import logout

_proximo_id = 1
TAREAS = []

ana = User(username='ana')
carlos = User(username='carlos')
lucia = User(username='lucia')


TAREAS= [
    Tarea(id=1, titulo="Comprar leche", descripcion="Ir al supermercado", creador=ana),
    Tarea(id=2, titulo="Estudiar Django", descripcion="Repasar vistas y formularios", creador=carlos),
    Tarea(id=3, titulo="Estudiar Bases de Datos", descripcion="Repasar contenido", creador=lucia),
]

_proximo_id = 4

def home_redirect(request):
    return redirect('/tareas/')
@login_required
def home(request):
    tareas_usuario = [
        t for t in TAREAS
        if t.creador.username == request.user.username
    ]
    return render(request, 'home.html', {'tareas': tareas_usuario})

@login_required
def detalles_tarea(request, tarea_id):
    tarea = next(
        (t for t in TAREAS if str(t.id) == str(tarea_id) and t.creador.username == request.user.username),
        None
    )
    if not tarea:
        return redirect('home')
    return render(request, 'detalles_tarea.html', {'tarea': tarea})

@login_required
def crear_tarea(request):
    global _proximo_id
    if request.method == 'POST':
        form = FormularioTareas(request.POST)
        if form.is_valid():

            nueva_tarea = Tarea(
                id=_proximo_id, 
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion'],
                creador=User(username=request.user.username)
            )
            TAREAS.append(nueva_tarea)
            _proximo_id += 1
            return redirect('home')
    else:
        form = FormularioTareas()
    return render(request, 'crear_tarea.html', {'form': form})

@login_required
def eliminar_tareas(request):
    tareas = [t for t in TAREAS if t.creador.username == request.user.username]
    return render(request, 'eliminar_tareas.html', {'tareas': tareas})

@login_required
def eliminar_tarea(request, tarea_id):
    global TAREAS
    TAREAS = [
        t for t in TAREAS
        if not (str(t.id) == str(tarea_id) and t.creador.username == request.user.username)
    ]
    return redirect('eliminar_tareas')

def logout_view(request):
    logout(request)
    return redirect('home') 