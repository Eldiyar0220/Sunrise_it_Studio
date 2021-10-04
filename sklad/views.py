from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from sklad.models import Sklad


class SkladViews(ListView):
    model = Sklad
    template_name = 'pages/index.html'
    context_object_name = 'sklads'