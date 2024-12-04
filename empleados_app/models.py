from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    curp=models.CharField(max_length=100)
    fecha_de_nacimiento=models.DateField(null=False,blank=False)
    num_celular=models.PositiveIntegerField()
    rfc=models.CharField(max_length=100)
    id_sucursales=models.PositiveIntegerField()
    direccion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre