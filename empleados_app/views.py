from django.shortcuts import render, redirect
from .models import Empleado

def inicio_vistaEmpleados(request):
    los_empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleados.html", {"mis_empleados": los_empleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    email = request.POST["txtemail"]
    curp = request.POST["txtcurp"]
    fecha_de_nacimiento = request.POST["txtacta"]
    num_celular = request.POST["txtcelular"]
    rfc = request.POST["txtrfc"]
    id_sucursales = request.POST["txtsucursal"]
    direccion = request.POST["txtdireccion"]

    Empleado.objects.create(
        id_empleado=id_empleado, nombre=nombre, email=email, curp=curp,
        fecha_de_nacimiento=fecha_de_nacimiento, num_celular=num_celular,
        rfc=rfc, id_sucursales=id_sucursales, direccion=direccion
    )
    return redirect("empleados")

def seleccionarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    fecha_de_nacimiento=empleado.fecha_de_nacimiento.strftime('%Y-%m-%d')
    return render(request,"editarEmpleado.html",{"mi_empleado":empleado, "mi_empleado" : empleado, "fecha_de_nacimiento" : fecha_de_nacimiento})

def editarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    email = request.POST["txtemail"]
    curp = request.POST["txtcurp"]
    fecha_de_nacimiento = request.POST["txtacta"]
    num_celular = request.POST["txtcelular"]
    rfc = request.POST["txtrfc"]
    id_sucursales = request.POST["txtsucursal"]
    direccion = request.POST["txtdireccion"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.email = email
    empleado.curp = curp
    empleado.fecha_de_nacimiento = fecha_de_nacimiento
    empleado.num_celular = num_celular
    empleado.rfc = rfc
    empleado.id_sucursales = id_sucursales
    empleado.direccion = direccion
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    empleado.delete()
    return redirect("empleados")
