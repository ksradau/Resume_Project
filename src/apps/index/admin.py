from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.index.models import UserInfo
from apps.index.models import MainPage


@admin.register(UserInfo)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(MainPage)
class MainPageAdminModel(ModelAdmin):
    pass