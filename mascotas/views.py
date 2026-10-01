"""
Vistas: CRUD completo del modelo principal (Mascota) + pagina de
categoria filtrada + pagina de horarios leidos desde JSON.

Listar y ver detalle: publico, no exige login.
Crear, editar, borrar: exigen login (LoginRequiredMixin).
"""
import json
from pathlib import Path

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import MascotaForm, CategoriaForm
from .models import Categoria, Mascota


class MascotaList(ListView):
    model = Mascota
    context_object_name = 'mascotas'


def mascotas_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    mascotas = Mascota.objects.filter(categoria=categoria)
    return render(request, 'mascotas/mascota_list.html', {
        'mascotas': mascotas,
        'categoria': categoria,
    })


class MascotaDetail(DetailView):
    model = Mascota


class MascotaCreate(LoginRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm
    success_url = reverse_lazy('mascota_list')


class MascotaUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm
    success_url = reverse_lazy('mascota_list')


class MascotaDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('mascota_list')


def horarios(request):
    ruta = Path(__file__).resolve().parent / 'data' / 'horarios.json'
    with open(ruta, encoding='utf-8') as f:
        datos = json.load(f)
    return render(request, 'mascotas/horarios.html', {'horarios': datos})

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('mascota_create')