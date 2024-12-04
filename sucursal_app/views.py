from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.
def inicio_vistaSucursales(request):
    las_sucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"sucursales": las_sucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["txtid"]
    id_empleado = request.POST["txtempleado"]
    contacto_s = request.POST["txtcontacto"]
    direccion_s = request.POST["txtdireccion"]
    correo_s = request.POST["txtcorreo"]
    horario = request.POST["txthorario"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        id_empleado=id_empleado,
        contacto_s=contacto_s,
        direccion_s=direccion_s,
        correo_s=correo_s,
        horario=horario,
    )

    return redirect("sucursales")

def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html", {"sucursal": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST["txtid"]
    id_empleado = request.POST["txtempleado"]
    contacto_s = request.POST["txtcontacto"]
    direccion_s = request.POST["txtdireccion"]
    correo_s = request.POST["txtcorreo"]
    horario = request.POST["txthorario"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.id_empleado = id_empleado
    sucursal.contacto_s = contacto_s
    sucursal.direccion_s = direccion_s
    sucursal.correo_s = correo_s
    sucursal.horario = horario
    sucursal.save()

    return redirect("sucursales")

def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursales")
