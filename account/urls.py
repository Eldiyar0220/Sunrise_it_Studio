from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView
from account import views
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', SignView.as_view(), name='login'),
    path('login/', views.Sign, name='login'),

    path('register/', views.register, name='register'),
    path('activate/', ActivationView.as_view(), name='activation'),

    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('edit_profile/', views.EditProfile, name='edit'),
    path('reset/<int:pk>/<str:token>/', views.reset, name='reset'),

    # path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # path('sign-up/', RegistrationView.as_view(), name='register'),
    path('myprofile/', profile, name='profile'),
    # path('success_registration/', views.SuccessfulRegistrationView.as_view(), name='successful-registration'),
    # path('activation/', views.ActivationView.as_view(), name='activation'),

    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    ]