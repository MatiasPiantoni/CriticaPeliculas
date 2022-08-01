from re import template
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from itertools import chain


from criticapelicula.models import Actor, Critica, Director, Pelicula
# Create your views here.
class ActorListView(generic.ListView):
    model = Actor

class ActorDetailView(generic.DetailView):
    model = Actor

class PeliculaListView(generic.ListView):
    model = Pelicula

class PeliculaDetailView(generic.DetailView):
    model = Pelicula

class DirectorListView(generic.ListView):
    model = Director

class DirectorDetailView(generic.DetailView):
    model = Director

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['peliculas']=Pelicula.objects.obetener_12_mejores()
        return context

class CriticasARevisarListView(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    permission_required = 'criticapelicula.can_mark_returned'
    model = Critica
    template_name ='criticapelicula/revisar-criticas.html'
    paginate_by = 10

class CriticaUpdate(UpdateView):
    model = Critica
    fields = ('estado',)
    success_url = reverse_lazy('revisar-criticas')
    template_name_suffix = '_update_form'

class CriticaCreate(CreateView):
    model = Critica
    fields = ['pelicula', 'nombre', 'email', 'puntaje_critica', 'comentario',]

class SearchResultsView(generic.ListView):
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get("q")
        pelicula_list = Pelicula.objects.filter(
            Q(nombre_pelicula__icontains=query) | Q(año_de_realizacion__icontains=query))
        return pelicula_list
