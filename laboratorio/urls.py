from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_lista, name='laboratorio_lista'),
    path('nuevo/', views.laboratorio_formulario, name='laboratorio_crear'),
    path('<int:id>/editar/', views.laboratorio_formulario, name='laboratorio_editar'),
    path('<int:id>/eliminar/', views.laboratorio_eliminar, name='laboratorio_eliminar'),
]
