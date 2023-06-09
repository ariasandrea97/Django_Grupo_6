# Generated by Django 4.2.1 on 2023-06-19 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excursion', models.CharField(max_length=128, verbose_name='Excursion')),
                ('detalle', models.CharField(max_length=1024, verbose_name='Detalle')),
                ('diasSalidas', models.CharField(max_length=1024, verbose_name='Dias Salidas')),
                ('duracion', models.CharField(max_length=10, verbose_name='Duracion')),
                ('horario', models.CharField(max_length=20, verbose_name='Horarios')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_hotel', models.CharField(max_length=128, verbose_name='Hotel')),
                ('direccion', models.CharField(max_length=128, verbose_name='Direccion')),
                ('categoria', models.IntegerField(verbose_name='Categoria')),
                ('descripcion', models.TextField(default='')),
                ('imagen', models.ImageField(default='default_image.jpg', upload_to='hoteles')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_restaurante', models.CharField(max_length=128, verbose_name='Restaurante')),
                ('direccion', models.CharField(max_length=128, verbose_name='Direccion')),
                ('categoria', models.IntegerField(verbose_name='Categoria')),
                ('detalle', models.CharField(max_length=1024, null=True, verbose_name='Detalle')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registracion', models.DateField(null=True)),
                ('fecha_desde', models.DateField(null=True)),
                ('fecha_hasta', models.DateField(null=True)),
                ('Tipo_reserva', models.CharField(choices=[('Alojamiento', 'Alojamiento'), ('Excursion', 'Excursion'), ('Gastronomia', 'Gastronomia')], default='Hotel', max_length=15, verbose_name='Tipo de reserva')),
                ('adulto', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2, verbose_name='Cantidad de Adultos')),
                ('menor', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Cantidad de Menores')),
                ('estado', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Viajeros.hotel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='ReservaRestaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registracion', models.DateField(null=True)),
                ('fecha_reserva', models.DateField(null=True)),
                ('Tipo_reserva', models.CharField(choices=[('Alojamiento', 'Alojamiento'), ('Excursion', 'Excursion'), ('Gastronomia', 'Gastronomia')], default='Gastronomia', max_length=15, verbose_name='Tipo de reserva')),
                ('adulto', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2, verbose_name='Cantidad de Adultos')),
                ('menor', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Cantidad de Menores')),
                ('estado', models.BooleanField(default=True)),
                ('restaurante', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='Viajeros.restaurante')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaExcursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registracion', models.DateField(null=True)),
                ('fecha_reserva', models.DateField(null=True)),
                ('hora_reserva', models.TimeField(null=True)),
                ('Tipo_reserva', models.CharField(choices=[('Alojamiento', 'Alojamiento'), ('Excursion', 'Excursion'), ('Gastronomia', 'Gastronomia')], default='Excursion', max_length=15, verbose_name='Tipo de reserva')),
                ('adulto', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2, verbose_name='Cantidad de Adultos')),
                ('menor', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Cantidad de Menores')),
                ('estado', models.BooleanField(default=True)),
                ('traslado', models.BooleanField(default=True)),
                ('excursion', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='Viajeros.excursion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='servicios',
            field=models.ManyToManyField(to='Viajeros.servicio'),
        ),
    ]
