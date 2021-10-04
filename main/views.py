from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from .forms import OrderCreateForm
from .models import *


class MainPageView(ListView):
    model = Sklad
    template_name = 'pages/index.html'
    context_object_name = 'posts'


class Countries_detail_view(DetailView):
    model = Country
    template_name = 'pages/shop.html'
    context_object_name = 'country'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postes'] = Post.objects.filter(country_id=self.slug)
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/detail-post.html'
    context_object_name = 'postes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.get_object().get_image
        context['images'] = self.get_object().images.exclude(id=image.id)
        return context

class PageFAQView(TemplateView):
    template_name = 'pages/FAQ.html'

class ConView(TemplateView):
    template_name = 'pages/con.html'


class PageAboutUsView(TemplateView):
    template_name = 'pages/about-us.html'

class PageShopView(ListView):
    model = Post
    template_name = 'pages/shop.html'
    context_object_name = 'postes'

class PageHowWorksView(TemplateView):
    template_name = 'pages/how-works.html'



class PageParcelView(ListView):
    model = Parcels
    template_name = 'pages/parcels.html'
    context_object_name = 'parcels'

class CreateNewPostView(CreateView):
    queryset = Post.objects.all()
    template_name = 'pages/parcels.html'
    form_class = OrderCreateForm
    context_object_name = 'create'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))


class SkladViews(ListView):
    model = Sklad
    template_name = 'pages/index.html'
    context_object_name = 'posts'


