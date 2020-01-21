from django.contrib import admin
from django.urls import path
from motor.views import index, register, login, logout, user_page, test_view, change_password, auto, add_model, add_seria, add_year, add_kuzov, add_cabinet, auto_profile, LK
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auto', auto, name='auto'),
    path('auto/<car>', add_model, name='add_model'),
    path('auto/<car>/<seria>', add_seria, name='add_seria'),
    path('auto/<car>/<seria>/<year>', add_year, name='add_year'),
    path('auto/<car>/<seria>/<year>/<kuzov>', add_kuzov, name='add_kuzov'),
    path('add_cabinet', add_cabinet, name='add_cabinet'),
    path('LK', LK, name='LK'),
    path('auto_profile', auto_profile, name='auto_profile'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('user_page', user_page, name='user_page'),
    path('test_view', test_view, name='test_view'),
    path('change_password', change_password, name='change_password')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
