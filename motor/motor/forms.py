from django import forms
from .models import User


# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)

    def clean_email(self):
        passed_email = self.cleaned_data.get('email', None)
        if User.objects.filter(Email=passed_email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return passed_email


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
