from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import User
from django.http import Http404


def index(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    user_id = request.session.get('user_id', None)
    if user_id is not None:
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise Http404('Error 404')
    params = None
    if user_id is None:
        params = {'signup_form': signup_form, 'login_form': login_form}
    else:
        params = {'user_login': user.Login}
    return render(request, 'motor/index.html', params)


def register(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        user = User()
        user.Email = signup_form.data.get("email", None)
        user.Login = signup_form.data.get("username", None)
        user.Password = signup_form.data.get('password', None)
        user.save()
        return redirect('index')
    return render(request, '/')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        email = login_form.data.get("email", None)
        password = login_form.data.get("password", None)
        user = User.objects.filter(Email=email, Password=password).first()
        if user is not None:
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            raise Http404('Error 404')
    raise Http404('Error 404')
