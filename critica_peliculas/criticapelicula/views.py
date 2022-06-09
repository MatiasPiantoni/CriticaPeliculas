from re import template
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from criticapelicula.models import Actor, Pelicula
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"