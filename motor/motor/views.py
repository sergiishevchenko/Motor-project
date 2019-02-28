from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserpageForm, PasswordForm
from .models import User
from django.http import Http404
from django import forms
import logging

logger = logging.getLogger(__name__)


class FormWrapper:
    def __init__(self, form, error=False):
        self.form = form
        self.error = error


def index(request):
    signup_form = FormWrapper(SignUpForm())
    login_form = FormWrapper(LoginForm())
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


def change_password(request):
    if request.method == 'POST':
        userpage_form = PasswordForm(request.POST)
        user_id = request.session.get('user_id', None)
        if user_id is None:
            return redirect('index')
        if userpage_form.is_valid():
            user = User.objects.filter(id=user_id)[0]
            if user is None:
                raise Http404('User {} not found'.format(user_id))
            user_password = user.Password
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')
            new_password2 = request.POST.get('new_password2')
            if password == user_password:
                if new_password == new_password2:
                    user.Password = new_password
            user.save()
            return redirect('change_password')
        else:
            raise Http404('Я в чем-то ошиблась')
    else:
        signup_form = FormWrapper(SignUpForm())
        login_form = FormWrapper(LoginForm())
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            user = User.objects.filter(id=user_id).first()
            if user is None:
                raise Http404('Error 404')
        params = None
        if user_id is None:
            params = {'signup_form': signup_form, 'login_form': login_form}
        else:
            params = {'user_login': user.Login, 'user_email': user.Email}
        return render(request, 'motor/change_password.html', params)


def user_page(request):
    if request.method == 'POST':
        userpage_form = UserpageForm(request.POST)
        user_id = request.session.get('user_id', None)
        if user_id is None:
            return redirect('index')
        if userpage_form.is_valid():
            user = User.objects.filter(id=user_id)[0]
            if user is None:
                raise Http404('User {} not found'.format(user_id))
            if 'email' in userpage_form.data:
                user.Email = userpage_form.data.get('email')
            if 'username' in userpage_form.data:
                user.Login = userpage_form.data.get('username')
            if 'firstname' in userpage_form.data:
                user.FirstName = userpage_form.data.get('firstname')
            if 'lastname' in userpage_form.data:
                user.LastName = userpage_form.data.get('lastname')
            if 'phone' in userpage_form.data:
                user.Phone = userpage_form.data.get('phone')
            if 'gender' in userpage_form.data:
                user.Gender = userpage_form.data.get('gender')
            user.save()
            return redirect('user_page')
        else:
            raise Http404('Я в чем-то ошиблась')
    else:
        signup_form = FormWrapper(SignUpForm())
        login_form = FormWrapper(LoginForm())
        user_id = request.session.get('user_id', None)
        if user_id is not None:
            user = User.objects.filter(id=user_id).first()
            if user is None:
                raise Http404('Error 404')
        params = None
        if user_id is None:
            params = {'signup_form': signup_form, 'login_form': login_form}
        else:
            params = {'user_login': user.Login, 'user_email': user.Email, 'firstname': user.FirstName,
                      'lastname': user.LastName, 'user_phone': user.Phone}
        return render(request, 'motor/user_page.html', params)


def register(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = User()
            user.Email = signup_form.data.get("email", None)
            user.Login = signup_form.data.get("username", None)
            user.Password = signup_form.data.get('password', None)
            user.save()
            return redirect('user_page')
        else:
            signup_form = FormWrapper(signup_form, True)
            login_form = FormWrapper(LoginForm())
            return render(request, 'motor/index.html', {'signup_form': signup_form, 'login_form': login_form})
    return render(request, '/')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        email = login_form.data.get("email", None)
        password = login_form.data.get("password", None)
        user = User.objects.filter(Email=email, Password=password).first()
        if user is not None:
            request.session['user_id'] = user.id
            return redirect('user_page')
        else:
            raise Http404('Error 404')
    raise Http404('Error 404')


def logout(request):
    if 'user_id' in request.session.keys():
        del request.session['user_id']
    return redirect('index')


def test_view(request):
    if request.method == 'POST':
        logger.debug('POST data: {}'.format(request.POST))
    elif request.method == 'GET':
        logger.debug('GET data: {}'.format(request.GET))
    else:
        raise RuntimeError('Invalid usage')
