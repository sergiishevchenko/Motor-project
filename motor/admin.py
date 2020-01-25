from django.contrib import admin

from .models import (User, UserGroup, AdvertiseCar)

admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(AdvertiseCar)
