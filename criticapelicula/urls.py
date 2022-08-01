from django.urls import path

from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('actores/', views.ActorListView.as_view(), name='actor'),
    path('actor/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),
    path('directores/', views.DirectorListView.as_view(), name='director'),    
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name='director-detail'),
    path('peliculas/', views.PeliculaListView.as_view(), name='pelicula'),
    path('pelicula/<int:pk>', views.PeliculaDetailView.as_view(), name='pelicula-detail'), 
    path('revisarcriticas/', views.CriticasARevisarListView.as_view(), name='revisar-criticas'), 
    path('critica/<int:pk>/update/', views.CriticaUpdate.as_view(), name='critica-update'), 
    path('critica/create/', views.CriticaCreate.as_view(), name='critica-create'), 
    path('search/', SearchResultsView.as_view(), name='search_results'), 
]