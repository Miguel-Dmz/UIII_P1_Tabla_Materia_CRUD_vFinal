from django.shortcuts import render, redirect
from .models import Ventas

# Vista principal para listar ventas
def inicio_vistaVentas(request):
    las_ventas = Ventas.objects.all()
    return render(request, "gestionarVentas.html", {"ventas": las_ventas})

# Registrar una nueva venta
def registrarVenta(request):
    id_venta = request.POST["txtidventa"]
    id_cliente = request.POST["txtidcliente"]
    id_calzado = request.POST["txtidcalzado"]
    fecha_venta = request.POST["txtfechaventa"]
    total = request.POST["txttotal"]
    id_empleado = request.POST["txtidempleado"]

    Ventas.objects.create(
        id_venta=id_venta,
        id_cliente=id_cliente,
        id_calzado=id_calzado,
        fecha_venta=fecha_venta,
        total=total,
        id_empleado=id_empleado,
    )
    return redirect("ventas")

# Seleccionar una venta para editar
def seleccionarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    fecha_venta=venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request,"editarVenta.html",{"venta":venta, "venta":venta,"fecha_venta":fecha_venta})

# Editar una venta
def editarVenta(request):
    id_venta = request.POST["txtidventa"]
    id_cliente = request.POST["txtidcliente"]
    id_calzado = request.POST["txtidcalzado"]
    fecha_venta = request.POST["txtfechaventa"]
    total = request.POST["txttotal"]
    id_empleado = request.POST["txtidempleado"]

    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_cliente = id_cliente
    venta.id_calzado = id_calzado
    venta.fecha_venta = fecha_venta
    venta.total = total
    venta.id_empleado = id_empleado
    venta.save()

    return redirect("ventas")

# Borrar una venta
def borrarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("ventas")
