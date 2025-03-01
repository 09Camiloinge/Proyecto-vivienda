# Generated by Django 5.1.6 on 2025-03-01 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_documento', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(default='correo@example.com', max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200)),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Unión Libre', 'Unión Libre')], max_length=20)),
                ('tipo_vinculacion', models.CharField(choices=[('Empleado', 'Empleado'), ('Independiente', 'Independiente'), ('Otro', 'Otro')], max_length=20)),
                ('ingresos', models.IntegerField(default=0)),
                ('egresos', models.IntegerField(default=0)),
                ('tipo_vivienda', models.CharField(choices=[('Propia', 'Propia'), ('Arrendada', 'Arrendada'), ('Familiar', 'Familiar')], max_length=20)),
                ('numero_habitantes', models.IntegerField()),
                ('descripcion_llegada', models.TextField(blank=True, null=True)),
                ('medio_transporte', models.CharField(blank=True, max_length=50, null=True)),
                ('predio_suelo', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
