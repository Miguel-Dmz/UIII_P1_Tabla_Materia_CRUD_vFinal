from django.shortcuts import render, redirect
from .models import Cliente

# Vista principal para listar clientes
def inicio_vistaClientes(request):
    los_clientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"clientes": los_clientes})

# Registrar un nuevo cliente
def registrarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    fecha_nacimiento = request.POST["txtfechanacimiento"]
    direccion = request.POST["txtdireccion"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        telefono=telefono,
        email=email,
        fecha_nacimiento=fecha_nacimiento,
        direccion=direccion,
    )
    return redirect("clientes")

# Seleccionar un cliente para editar
def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    fecha_nacimiento=cliente.fecha_nacimiento.strftime('%Y-%m-%d')
    return render(request,"editarCliente.html",{"cliente":cliente, "cliente":cliente,"fecha_nacimiento":fecha_nacimiento})

# Editar un cliente
def editarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    fecha_nacimiento = request.POST["txtfechanacimiento"]
    direccion = request.POST["txtdireccion"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.telefono = telefono
    cliente.email = email
    cliente.fecha_nacimiento = fecha_nacimiento
    cliente.direccion = direccion
    cliente.save()

    return redirect("clientes")

# Borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")
