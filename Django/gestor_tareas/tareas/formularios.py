from django import forms
from .models import Tarea

class FormularioTareas(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Escribe el nombre de tu tarea',
            'descripcion': 'Escribe de qué trata',
        }