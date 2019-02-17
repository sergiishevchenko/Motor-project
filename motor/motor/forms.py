from django import forms
from .models import User

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

CHOICES = (
    ('man', 'woman'),
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
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    gender = forms.ChoiceField(choices=CHOICES)
    address = forms.CharField(label='Address')
    country = forms.CharField(label='Country')
    city = forms.CharField(label='City')
    mobile = forms.RegexField(label='Mobile', regex=r'^\+*\d{11}$')
