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
    list_display = ('apellido', 'nombre', 'edad_actor', 'fecha_de_nacimiento', 'admin_foto', )
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'biografia_actor', 'foto_actor', 'admin_foto', ]
    inlines = [RoleInline]
    search_fields = ("apellido__startswith", )
    readonly_fields = ('admin_foto', )
    
class PeliculasDirigidasInline(admin.TabularInline):
    model = Pelicula
    verbose_name = 'Pelicula Dirigida'
    verbose_name = 'Peliculas Dirigida'
    extra = 0
    fields = ['nombre_pelicula', 'año_de_realizacion', 'actores', 'genero', 'admin_foto', ]
    readonly_fields = ('admin_foto', ) 
   
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'edad_director', 'fecha_de_nacimiento', 'admin_foto', )
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'biografia_director', 'foto_director', 'admin_foto', ]
    inlines = [PeliculasDirigidasInline] 
    search_fields = ("apellido__startswith", )
    readonly_fields = ('admin_foto', )

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre_pelicula', 'año_de_realizacion', 'genero', 'director', 'puntaje_pelicula', 'admin_foto', )
    fields = ['nombre_pelicula', 'año_de_realizacion', 'genero', 'resumen', 'actores', 'director', 'foto_pelicula', 'admin_foto', ] 
    search_fields = ("nombre_pelicula__startswith", )
    readonly_fields = ('admin_foto', )
    filter_horizontal = ('actores',)

@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'nombre', 'email', 'puntaje_critica')
    fields = ['pelicula', 'nombre', 'email', 'puntaje_critica', 'comentario', 'estado'] 
    search_fields = ("email__startswith", )   
