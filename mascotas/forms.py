"""
ModelForm del modelo principal (Mascota). Se usa tanto para crear como
para editar (MascotaCreate y MascotaUpdate, en views.py).
"""
from django import forms

from .models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'categoria', 'raza', 'edad', 'descripcion', 'imagen', 'disponible']