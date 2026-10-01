"""
Modelos: dos modelos relacionados.

- Categoria: modelo de clasificacion (ej: Perros, Gatos, Aves).
- Mascota: modelo principal, con ForeignKey hacia Categoria.
"""

from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='mascotas')
    raza = models.CharField(max_length=60, blank=True)
    edad = models.PositiveSmallIntegerField(help_text='Edad en años')
    descripcion = models.TextField(blank=True)
    imagen = models.URLField(max_length=500, help_text='URL de una foto de la mascota')
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-disponible', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.categoria})'