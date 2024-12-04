from django.urls import path
from calzado_app import views

urlpatterns = [
    path("calzados", views.inicio_vistaCalzados, name="calzados"),
    path("registrarCalzado/", views.registrarCalzado, name="registrarCalzado"),
    path("seleccionarCalzado/<codigo>", views.seleccionarCalzado, name="seleccionarCalzado"),
    path("editarCalzado/", views.editarCalzado, name="editarCalzado"),
    path("borrarCalzado/<codigo>", views.borrarCalzado, name="borrarCalzado"),
]
