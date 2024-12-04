# Generated by Django 5.1.3 on 2024-12-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calzado',
            fields=[
                ('id_calzado', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_c', models.CharField(max_length=100)),
                ('material_c', models.CharField(max_length=100)),
                ('talla_c', models.CharField(max_length=100)),
                ('precio_c', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color_C', models.CharField(max_length=100)),
                ('tipo_c', models.CharField(max_length=100)),
                ('modelo_c', models.CharField(max_length=100)),
            ],
        ),
    ]
