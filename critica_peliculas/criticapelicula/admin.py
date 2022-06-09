from django.contrib import admin
# Register your models here.
from .models import Actor, Director, Pelicula, Critica

class RoleInline(admin.TabularInline):
    model = Pelicula.actores.through
    verbose_name = 'Rol'
    verbose_name_plural = 'Roles'
    extra = 0

@admin.register(Actor)
class ActoresAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'edad_actor', 'fecha_de_nacimiento')
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'edad_actor', 'biografia_actor', 'foto_actor']
    inlines = [RoleInline]


class PeliculasDirigidasInline(admin.TabularInline):
    model = Pelicula
    verbose_name = 'Pelicula Dirigida'
    verbose_name = 'Peliculas Dirigidas'
    extra = 0

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'edad_director', 'fecha_de_nacimiento')
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'edad_director', 'biografia_director', 'foto_director']
    inlines = [PeliculasDirigidasInline]


class CriticasInline(admin.TabularInline):
    model = Critica
    verbose_name = 'Critica'
    verbose_name_plural = 'Criticas'
    extra = 0

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre_pelicula', 'año_de_realizacion', 'genero', 'director', 'puntaje_pelicula')
    fields = ['nombre_pelicula', 'año_de_realizacion', 'genero', 'resumen', 'director', 'foto_pelicula'] 
    inlines = [RoleInline, CriticasInline]


@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'nombre', 'email', 'puntaje_critica')
    fields = ['pelicula', 'nombre', 'email', 'puntaje_critica', 'comentario']    
