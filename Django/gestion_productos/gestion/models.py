from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    dimensiones = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.dimensiones} - {self.peso}kg"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Relación Muchos a Uno
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")

    # Relación Muchos a Muchos
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name="productos")

    # Relación Uno a Uno
    detalle = models.OneToOneField(
        Detalle,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="producto"
    )

    def __str__(self):
        return self.nombre