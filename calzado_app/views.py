from django.shortcuts import render, redirect
from .models import Calzado

def inicio_vistaCalzados(request):
    los_calzados = Calzado.objects.all()
    return render(request, "gestionarCalzado.html", {"mis_calzados": los_calzados})

def registrarCalzado(request):
    id_calzado = request.POST["txtcodigo"]
    nombre_c = request.POST["txtnombre"]
    material_c = request.POST["txtmaterial"]
    talla_c = request.POST["txttalla"]
    precio_c = request.POST["txtprecio"]
    color_C = request.POST["txtcolor"]
    tipo_c = request.POST["txttipo"]
    modelo_c = request.POST["txtmodelo"]

    Calzado.objects.create(
        id_calzado=id_calzado, nombre_c=nombre_c, material_c=material_c,
        talla_c=talla_c, precio_c=precio_c, color_C=color_C, tipo_c=tipo_c,
        modelo_c=modelo_c
    )
    return redirect("calzados")

def seleccionarCalzado(request, codigo):
    calzado = Calzado.objects.get(id_calzado=codigo)
    return render(request, "editarCalzado.html", {"mi_calzado": calzado})

def editarCalzado(request):
    id_calzado = request.POST["txtcodigo"]
    nombre_c = request.POST["txtnombre"]
    material_c = request.POST["txtmaterial"]
    talla_c = request.POST["txttalla"]
    precio_c = request.POST["txtprecio"]
    color_C = request.POST["txtcolor"]
    tipo_c = request.POST["txttipo"]
    modelo_c = request.POST["txtmodelo"]

    calzado = Calzado.objects.get(id_calzado=id_calzado)
    calzado.nombre_c = nombre_c
    calzado.material_c = material_c
    calzado.talla_c = talla_c
    calzado.precio_c = precio_c
    calzado.color_C = color_C
    calzado.tipo_c = tipo_c
    calzado.modelo_c = modelo_c
    calzado.save()
    return redirect("calzados")

def borrarCalzado(request, codigo):
    calzado = Calzado.objects.get(id_calzado=codigo)
    calzado.delete()
    return redirect("calzados")
