from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, Detalle


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    list_filter = ('categoria', 'etiquetas')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('etiquetas',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('dimensiones', 'peso')