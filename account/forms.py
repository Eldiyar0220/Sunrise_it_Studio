from django.utils.crypto import get_random_string
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail


User = get_user_model()

def send_activation_mail(email):
    message = f'http://127.0.0.1:8000/account/activate/'
    send_mail('Активация аккаунта', message, 'test@gmail.com', [email])


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'sign__input required','type':'text','id':"reg-email", 'name':"reg-email", 'placeholder':'Email или ваша почта'}))
    password = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'sign__input','placeholder':'Пароль'}))
    password_confirm = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'sign__input','placeholder':'Повторите пароль'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'имя'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Фамилия'}))
    before_last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Отчество'}))
    address_living = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Аддрес проживание'}))
    city = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Город'}))
    number_of_address = forms.CharField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'номер'}))
    postal_code = forms.CharField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'индекс'}))
    # passport_out = forms.CharField(required=True, widget=forms.NumberInput(attrs={'type': 'file', 'class': 'sign__input ','name': '','accept': 'image/*'}))
    # passport_in = forms.ImageField(required=True, widget=forms.FileInput(attrs={'type': 'file','class': 'sign__input file__upload','id': 'scan-in','name': '','accept': 'image/*'}))
    phone_number = forms.CharField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'Ваш номер телефона'}))
    telegram = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'@Nickname'}))

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password',
                   'password_confirm', 'last_name', 'before_last_name',
                   'address_living', 'city', 'number_of_address',
                   'postal_code', 'telegram', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь уже зарегестрировался ')
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def clean_phone(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.startswith('+996'):
            raise forms.ValidationError('Номер должен начинатся с +996')
        if len(phone) != 13:
            raise forms.ValidationError('Ошибка only 13 ')
        return phone



    def save(self):
        user = User.objects.create(**self.cleaned_data)
        user.create_activation_code()
        send_activation_mail(user.email)
        return user


class SignForm(forms.Form):
    email = forms.EmailField(max_length=200,required=True, widget=forms.TextInput(attrs={ 'class': 'sign__input', 'type': 'text','id':"sign-email", 'placeholder': 'Email или ваша почта' }))
    password = forms.CharField(min_length=8,required=True, widget=forms.PasswordInput(attrs={ 'class': 'sign__input', 'placeholder': 'Пароль!!' }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Email не найден попробуйте снова')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
        return super().clean(*args, **kwargs)


class ChangePasswordForm(forms.Form):
    old_pass  = forms.CharField(min_length=8,required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'sign__input',
                                    'type':"password",
                                    'placeholder': 'Пароль'
                                }))
    new_pass = forms.CharField(min_length=8,required=True, widget=forms.PasswordInput(attrs={ 'class': 'sign__input','type':"password", 'placeholder': 'Пароль' }))
    new_pass_confirm = forms.CharField(min_length=8,required=True, widget=forms.PasswordInput(attrs={ 'class': 'sign__input','type':"password", 'placeholder': 'Пароль' }))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean_old_pass(self):
        old_pass = self.cleaned_data.get('old_pass')
        user = self.request.user
        if not user.check_password(old_pass):
            raise forms.ValidationError('Укажите верный пароль')
        return old_pass

    def clean(self):
        new_pass = self.cleaned_data.get('new_pass')
        new_pass_confirm = self.cleaned_data.get('new_pass_confirm')
        if new_pass != new_pass_confirm:
            raise forms.ValidationError('Неверное подтверждение пароля')
        return self.cleaned_data

    def save(self):
        new_pass = self.cleaned_data.get('new_pass')
        user = self.request.user
        user.set_password(new_pass)
        user.save()


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'sign__input',
            'type': 'text',
            'placeholder': 'forgotmer@gmail.com!!',
            }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователя не существует')
        return email

    def send_new_password(self):
        email = self.cleaned_data.get('email')
        new_pass = get_random_string(15, 'GLOBAL0123456789')
        user = User.objects.get(email=email)
        user.set_password(new_pass)
        user.save()
        send_mail(f'{email}',
                  f'Bы можете легко вернуть свой аккаунт: Здравствуйте, {email} Очень жаль, что вы не можете войти в GlobalExpress. Мы можем помочь вам восстановить доступ к вашему аккаунту,'
                  f'Ваш новый пароль: {new_pass}', 'test@gmail.com', [email])


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_name', 'before_last_name', 'address_living', 'city', 'number_of_address', 'postal_code' ,'phone_number']



class ResetForm(forms.Form):
    new_pass = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(
        attrs={ 'class': 'sign__input', 'type': "password", 'placeholder': 'Пароль' }))
    new_pass_confirm = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(
        attrs={ 'class': 'sign__input', 'type': "password", 'placeholder': 'Пароль' }))

    def new_password(self):
        password = self.cleaned_data.get('new_pass')
        password2 = self.cleaned_data.pop('new_pass_confirm')
        if password != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data







