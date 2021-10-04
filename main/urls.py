from django.urls import path

from .views import *

urlpatterns = [
   path('', MainPageView.as_view(), name='home'),
   path('faq/', PageFAQView.as_view(), name='faq'),
   path('about-us/', PageAboutUsView.as_view(), name='about'),
   path('shop/', PageShopView.as_view(), name='shop'),
   path('how-works?/', PageHowWorksView.as_view(), name='works'),
   path('parcels/', PageParcelView.as_view(), name='parsel'),
   path('countries/<str:slug>/', Countries_detail_view.as_view(), name='country'),
   path('detail-posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
   # path('detail-news/<int:pk>/', NewsDetailView.as_view(), name='news'),
   path('create/', CreateView.as_view(), name='works'),
   path('con/', ConView.as_view(), name='con'),

]