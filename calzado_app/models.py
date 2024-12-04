from django.db import models

# Create your models here.
class Calzado(models.Model):
    id_calzado=models.PositiveIntegerField(primary_key=True)
    nombre_c=models.CharField(max_length=100)
    material_c=models.CharField(max_length=100)
    talla_c=models.CharField(max_length=100)
    precio_c=models.DecimalField(max_digits=10, decimal_places=2)
    color_C=models.CharField(max_length=100)
    tipo_c=models.CharField(max_length=100)
    modelo_c=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_c