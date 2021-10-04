from django.urls import path

from .views import *

urlpatterns = [
   path('', SkladViews.as_view(), name='efrthy')
   ]