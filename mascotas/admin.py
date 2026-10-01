from django.contrib import admin

from .models import Categoria, Mascota


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'raza', 'edad', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'raza')
