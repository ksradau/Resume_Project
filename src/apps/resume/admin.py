from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.resume.models import ResumePage


@admin.register(ResumePage)
class ResumePageAdminModel(ModelAdmin):
    pass