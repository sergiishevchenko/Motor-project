from django import forms
from .models import User

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

CHOICES = (
    ('М', 'man'),
    ('Ж', 'woman')
)


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)

    def clean_email(self):
        passed_email = self.cleaned_data.get('email', None)
        if User.objects.filter(Email=passed_email).count() > 0:
            raise forms.ValidationError(u'Данный email уже используется.')
        return passed_email

    def clean_username(self):
        passed_username = self.cleaned_data.get('username', None)
        if User.objects.filter(Login=passed_username).count() > 0:
            raise forms.ValidationError(u'Данный логин занят.')
        return passed_username


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)


class UserpageForm(forms.Form):
    email = forms.EmailField(max_length=256)
    username = forms.CharField(label='Username', min_length=4, max_length=150)
    firstname = forms.CharField(label='First name')
    lastname = forms.CharField(label='Last name')
    gender = forms.ChoiceField(choices=CHOICES)
    phone = forms.RegexField(label='Phone', regex=r'^\+*\d{11}$')

    def clean_password(self):
        passed_password = self.cleaned_data.get('password', None)
        passed_email = self.cleaned_data.get('email', None)
        if User.objects.filter(Email=passed_email, Password=passed_password).count() == 0:
            raise forms.ValidationError(u'Invalid email or password')
        return passed_password


class PasswordForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='New Password2', widget=forms.PasswordInput)

    # def clean_password(self):
    #     passed_password = self.cleaned_data.get('password', None)
    #     passed_email = self.cleaned_data.get('email', None)
    #     if User.objects.filter(Email=passed_email, Password=passed_password).count() == 0:
    #         raise forms.ValidationError(u'Invalid email or password')
    #     return passed_password
