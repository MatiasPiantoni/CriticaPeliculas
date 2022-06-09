# Generated by Django 4.0.4 on 2022-06-01 02:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='ingrese el nombre del actor', max_length=100)),
                ('apellido', models.CharField(help_text='ingrese el apellido del actor', max_length=100)),
                ('biografia_actor', models.TextField(max_length=300)),
                ('foto_actor', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='ingrese el nombre del director', max_length=100)),
                ('apellido', models.CharField(help_text='ingrese el apellido del director', max_length=100)),
                ('biografia_director', models.TextField(max_length=300)),
                ('foto_director', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pelicula', models.CharField(help_text='ingrese el nombre de la pelicula', max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('actores', models.ManyToManyField(to='criticapelicula.actor')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='criticapelicula.director')),
            ],
        ),
        migrations.CreateModel(
            name='Critica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('comentario', models.TextField(max_length=100)),
                ('puntaje_critica', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('email', models.CharField(max_length=100)),
                ('pelicula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='criticapelicula.pelicula')),
            ],
        ),
    ]