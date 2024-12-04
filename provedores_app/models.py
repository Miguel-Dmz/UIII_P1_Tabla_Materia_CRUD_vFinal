from django.db import models

# Create your models here.
class Provedor(models.Model):
    id_provedor=models.PositiveIntegerField(primary_key=True)
    empresa=models.CharField(max_length=50)
    num_celular=models.PositiveIntegerField()
    email=models.EmailField(max_length=50)
    id_sucursal=models.PositiveIntegerField()
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)

    def __str__(self):
        return self.id_provedor