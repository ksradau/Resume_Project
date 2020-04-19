from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.education.models import EducationPage


@admin.register(EducationPage)
class EducationPageAdminModel(ModelAdmin):
    pass
