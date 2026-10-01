from django.urls import path

from . import views

urlpatterns = [
    path('', views.MascotaList.as_view(), name='mascota_list'),
    path('categoria/<int:pk>/', views.mascotas_por_categoria, name='mascota_por_categoria'),
    path('horarios/', views.horarios, name='horarios'),
    path('nueva/', views.MascotaCreate.as_view(), name='mascota_create'),
    path('<int:pk>/', views.MascotaDetail.as_view(), name='mascota_detail'),
    path('<int:pk>/editar/', views.MascotaUpdate.as_view(), name='mascota_update'),
    path('<int:pk>/borrar/', views.MascotaDelete.as_view(), name='mascota_delete'),
    path('categorias/nueva/', views.CategoriaCreate.as_view(), name='categoria_create'),
]