from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=datetime.now)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    class Meta:
        #Creando permisos adicionales
        permissions = [
            ("ver_mis_tareas", "Ver tareas propias")

        ]

    def __str__(self):
        return self.titulo
