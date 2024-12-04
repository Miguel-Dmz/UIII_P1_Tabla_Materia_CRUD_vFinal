from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes", views.inicio_vistaClientes, name="clientes"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<int:id_cliente>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<int:id_cliente>", views.borrarCliente, name="borrarCliente"),
]
