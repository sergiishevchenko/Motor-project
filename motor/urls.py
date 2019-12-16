"""motor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from motor.views import index, register, login, logout, user_page, test_view, change_password, auto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('auto', auto, name='auto'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('user_page', user_page, name='user_page'),
    path('test_view', test_view, name='test_view'),
    path('change_password', change_password, name='change_password')
]
