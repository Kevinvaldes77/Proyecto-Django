from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionFicha/<codigo>', views.edicionFicha),
    path('editarFicha/', views.editarFicha),
    path('eliminarFicha/<codigo>', views.eliminarFicha),
]