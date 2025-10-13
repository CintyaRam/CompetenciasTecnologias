from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('detalles-tarea/<int:tarea_id>/', views.detalles_tarea, name="detalles_tarea"),
    path('crear-tarea/', views.crear_tarea, name="crear_tarea"),
    path('eliminar/', views.eliminar_tareas, name='eliminar_tareas'),
    path('eliminar-tarea/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    

]