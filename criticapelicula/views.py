from re import template
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from criticapelicula.models import Actor, Pelicula
# Create your views here.
class ActorListView(generic.ListView):
    model = Actor

class ActorDetailView(generic.DetailView):
    model = Actor

class PeliculaDetailView(generic.DetailView):
    model = Pelicula

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['peliculas']=Pelicula.objects.obetener_12_mejores()
        return context