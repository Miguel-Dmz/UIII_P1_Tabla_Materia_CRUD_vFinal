# Generated by Django 5.1.3 on 2024-12-04 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('id_empleado', models.PositiveIntegerField()),
                ('contacto_s', models.PositiveIntegerField()),
                ('direccion_s', models.CharField(max_length=100)),
                ('correo_s', models.EmailField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
            ],
        ),
    ]