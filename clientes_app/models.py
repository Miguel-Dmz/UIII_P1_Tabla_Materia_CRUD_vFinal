from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    email=models.EmailField(max_length=50)
    fecha_nacimiento=models.DateField(null=False,blank=False)
    direccion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre