from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.index.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdminModel(ModelAdmin):
    pass
