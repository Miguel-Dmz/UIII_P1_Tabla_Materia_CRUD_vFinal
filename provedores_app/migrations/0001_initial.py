# Generated by Django 5.1.3 on 2024-12-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id_provedor', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('empresa', models.CharField(max_length=50)),
                ('num_celular', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('id_sucursal', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
