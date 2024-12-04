from django.shortcuts import render, redirect
from .models import Provedor

def inicio_vistaProvedores(request):
    los_provedores = Provedor.objects.all()
    return render(request, "gestionarProvedor.html", {"mis_provedores": los_provedores})

def registrarProvedor(request):
    id_provedor = request.POST["txtcodigo"]
    empresa = request.POST["txtempresa"]
    num_celular = request.POST["txtcelular"]
    email = request.POST["txtemail"]
    id_sucursal = request.POST["txtsucursal"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]

    Provedor.objects.create(
        id_provedor=id_provedor,
        empresa=empresa,
        num_celular=num_celular,
        email=email,
        id_sucursal=id_sucursal,
        nombre=nombre,
        direccion=direccion,
    )
    return redirect("provedores")

def seleccionarProvedor(request, codigo):
    provedor = Provedor.objects.get(id_provedor=codigo)
    return render(request, "editarProvedor.html", {"mi_provedor": provedor})

def editarProvedor(request):
    id_provedor = request.POST["txtcodigo"]
    empresa = request.POST["txtempresa"]
    num_celular = request.POST["txtcelular"]
    email = request.POST["txtemail"]
    id_sucursal = request.POST["txtsucursal"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]

    provedor = Provedor.objects.get(id_provedor=id_provedor)
    provedor.empresa = empresa
    provedor.num_celular = num_celular
    provedor.email = email
    provedor.id_sucursal = id_sucursal
    provedor.nombre = nombre
    provedor.direccion = direccion
    provedor.save()
    return redirect("provedores")

def borrarProvedor(request, codigo):
    provedor = Provedor.objects.get(id_provedor=codigo)
    provedor.delete()
    return redirect("provedores")
