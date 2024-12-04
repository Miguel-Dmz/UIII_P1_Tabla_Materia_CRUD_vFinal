from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal=models.PositiveIntegerField(primary_key=True)
    id_empleado=models.PositiveIntegerField()
    contacto_s=models.PositiveIntegerField()
    direccion_s=models.CharField(max_length=100)
    correo_s=models.EmailField(max_length=50)
    horario=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_sucursal