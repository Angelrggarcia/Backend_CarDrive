# Generated by Django 5.0.4 on 2024-05-14 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDriveBk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiquetas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=32)),
                ('descripcion', models.CharField(max_length=150)),
                ('terminacion', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('id_apartados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.apartado')),
                ('id_usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_apartado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.apartado')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Asociar_etiquetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_archivos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.archivos')),
                ('id_etiquetas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.etiquetas')),
            ],
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.archivos')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_apartado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.apartado')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Proyectleader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.proyecto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Recientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.DateTimeField()),
                ('id_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.archivos')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteracion', models.IntegerField()),
                ('archivo', models.BinaryField()),
                ('id_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarDriveBk.archivos')),
            ],
        ),
    ]