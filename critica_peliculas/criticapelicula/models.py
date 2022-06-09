from asyncio.windows_events import NULL
from django.db.models import Avg
from audioop import avg
from tkinter import CASCADE
from django.db import models
from django.db.models.functions import Round
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Director (models.Model):

    nombre = models.CharField (max_length=100, help_text='ingrese el nombre del director')
    apellido = models.CharField (max_length=100, help_text='ingrese el apellido del director')
    edad_director = models.IntegerField (default=18,validators=[MinValueValidator(18),MaxValueValidator(120)])
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    biografia_director = models.TextField (max_length=1000)
    foto_director = models.ImageField(blank=True, upload_to='media') 
    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Actor (models.Model):

    nombre = models.CharField (max_length=100, help_text='ingrese el nombre del actor')
    apellido = models.CharField (max_length=100, help_text='ingrese el apellido del actor')
    edad_actor = models.IntegerField (default=18,validators=[MinValueValidator(5),MaxValueValidator(120)])
    fecha_de_nacimiento = models.DateField(null=True, blank=True) 
    biografia_actor = models.TextField (max_length=1000) 
    foto_actor = models.ImageField (blank=True, upload_to='media')
    class Meta:
        verbose_name_plural = 'Actores'
    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Pelicula (models.Model):

    nombre_pelicula = models.CharField (max_length=100, help_text='ingrese el nombre de la pelicula')
    resumen = models.TextField (max_length=1000, default=NULL) 
    año_de_realizacion = models.DateField (null=True, blank=True)
    actores = models.ManyToManyField (Actor)
    director = models.ForeignKey (Director, on_delete=models.SET_NULL, null=True) 
    puntaje_pelicula = models.IntegerField (default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    genero = models.CharField(max_length=50)
    foto_pelicula = models.ImageField(blank=True, upload_to='media')
    def get_puntaje(self, *args):
        critica = list(Critica.objects.filter(pelicula= self.id).aggregate(Avg('puntaje_critica')).values())[0]
        self.puntaje_pelicula = critica
        Round(self.puntaje_pelicula, 1)
        return self.puntaje_pelicula 

    def get_absolute_url(self):
        return reverse('pelicula-detail', args=[str(self.id)])
    def __str__(self):
        return self.nombre_pelicula


class Critica (models.Model):

    nombre = models.CharField (max_length=100)
    pelicula = models.ForeignKey (Pelicula, on_delete=models.SET_NULL, null=True)
    comentario = models.TextField (max_length=100)
    puntaje_critica = models.IntegerField (default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    email = models.CharField (max_length=100)
    
    ESTADO_COMENTARIO = (
        ('e', 'En Espera'),
        ('a', 'Aceptado'),
        ('r', 'Rechazado'),
    )

    estado = models.CharField(max_length=1, choices=ESTADO_COMENTARIO, default='e')

    def save(self, *args, **kwargs):
        super(Critica, self).save(*args, **kwargs) 
        peli = self.pelicula
        peli.get_puntaje(self.pelicula)
        peli.save()
    def get_absolute_url(self):
        return reverse('critica-detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.pelicula}, {self.email}'