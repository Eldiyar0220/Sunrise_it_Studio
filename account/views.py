from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View, generic
from django.views.generic import TemplateView, UpdateView, edit, FormView, CreateView

from . import models
from .forms import UserRegistrationForm, ChangePasswordForm, ForgotPasswordForm, SignForm, UserEditForm, ResetForm
from .models import User

def  register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            print(user_form.is_valid())
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse('Вы успешно зарегистрировались !!!')
            # return render(request, 'users/registration.html', {'new_user': new_user})
        return render(request, 'account/registration.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/registration.html', {'user_form': user_form})

class ActivationView(View):
    def get(self, request):

        return render(request, 'account/activation.html', {})

# class RegisterView(FormView):
#     model = User
#     form_class = UserRegistrationForm
#     template_name = 'account/registration.html'
#     context = {
#         'user_form':form_class
#     }
#     success_url = reverse_lazy('home')




def profile(request):
    return render(request, 'account/personal-area.html')
#

# class SignView(LoginView):
#     template_name = 'account/sign.html'
#     def Sign(self, request):
#         form1 = ForgotPasswordForm()
#         if request.method == 'POST':
#             form = SignForm(data=request.POST)
#
#             if form.is_valid():
#                 email = form.cleaned_data.get('email')
#                 password = form.cleaned_data.get('password')
#                 user = authenticate(username=email, password=password)
#                 login(request, user)
#                 return redirect('home')
#
#         else:
#             form = SignForm()
#         return render(request, 'account/sign.html', {'form': form,'form1':form1})
def Sign(request):
    form1 = ForgotPasswordForm()
    if request.method == 'POST':
        form = SignForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = SignForm()
    return render(request, 'account/sign.html', {'form': form,'form1':form1})


class ChangePasswordView(TemplateView):
    template_name = 'account/personal-area.html'
    def post(self, request):
        if request.method == 'POST':
            user_form = ChangePasswordForm(request.POST, request=request)
            if user_form.is_valid():
                user_form.save()
            return render(request, 'account/personal-area.html', { 'user_form': user_form })
        else:
            user_form = ChangePasswordForm()
        return render(request, 'account/personal-area.html', {'user_form': user_form})



# class ForgotPasswordView(View):
#     template_name = 'pages/sssign.html'
#     def post(self, request):
#         if request.method == 'POST':
#             form1 = ForgotPasswordForm(request.POST)
#             print('hello')
#             if form1.is_valid():
#                 print('sadfasss')
#                 form1.send_new_password()
#             return HttpResponse('successfully send to you email ')
#
#     def get(self, request):
#         form1 = ForgotPasswordForm()args
#         return render(request, 'pages/sssign.html',{'form1': form1})

# class ForgotPasswordView(View):
#     @staticmethod
#     def get(request, *args, **kwargs):
#         email = request.GET.get('email')
#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             new_pass = get_random_string(15, 'GLOBAL0123456789')
#             user.set_password(new_pass)
#             user.save()
#             send_mail(f'{user}',
#                       f'Bы можете легко вернуть свой аккаунт: {new_pass}Здравствуйте, {email} Очень жаль, что вы не можете войти в GlobalExpress. Мы можем помочь вам восстановить доступ к вашему аккаунту,'
#                       f'Ваш новый пароль:', 'test@gmail.com', [email])
#             return JsonResponse({'data': True},status=200)
#         else:
#             return JsonResponse({'data': False})



class ForgotPasswordView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        email = request.GET.get('email')
        print(1)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            pk = user.id
            token = user.password
            token = token.replace('/', '')
            url = f'{request.get_host()}{reverse("reset", args=[pk, token])}'
            send_mail("Изменение пароля", f'Чтобы изменить пароль, перейдите по ссылке => {url}',
                      'test@mail.ru', [email], fail_silently=False)
            return JsonResponse({'data': True},status=200)
        else:
            return JsonResponse({'data': False})

def reset(request, pk, token):
    user = User.objects.get(id=pk)
    print(1,user)
    token_db = user.password.replace('/','')
    form = ResetForm()
    if token_db == token and request.method == 'GET':
        return render(request, 'account/reset_password.html', {'form':form})
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('new_pass')
            user.set_password(password)
            user.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'pages/error/404.htm')

def registerr(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            new_pass = user_form.save(commit=True)
            new_pass.set_password(user_form.cleaned_data['password'])
            new_pass.save()
            return HttpResponse('successfully registered')
        return render(request, 'html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'html', {'user_form': user_form})














# class EditProfileView(generic.UpdateView):
#     queryset = User.objects.all()
#     template_name = 'pages/edi-profile.html'
#     form_class = UserEditForm
#     context_object_name = 'edit'
#
#     def get_success_url(self):
#         return reverse('change-password', args=(self.object.id,))
# class EditProfileView(UpdateView):
#     template_name = 'pages/edi-profile.html'
#     fields = ['email','username', 'last_name','before_last_name','city','address_living','number_of_address','postal_code']
#     context_object_name = 'edit'
def EditProfile(request):
    if request.method == 'POST':
        edit = UserEditForm(request.POST,request.FILES,instance=request.user)
        if edit.is_valid():

            edit.save()
        return render(request, 'account/edi-profile.html', {'edit':edit})
    else:
        edit = UserEditForm(instance=request.user)
    return render(request, 'account/edi-profile.html',{'edit':edit} )

    # def get_queryset(self):
    #     """Return Schools """
    #     return models.User.objects.order_by('id')
    # def get_success_url(self):
    #     """Redirect"""
    #     return reverse('home')







#------------------------------------just



















