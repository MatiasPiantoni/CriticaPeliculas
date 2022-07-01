from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('actores/', views.ActorListView.as_view(), name='actor'),
    path('actor/<int:pk>', views.ActorDetailView.as_view(), name='actor-detail'),
    path('pelicula/<int:pk>', views.PeliculaDetailView.as_view(), name='pelicula-detail'),     
]