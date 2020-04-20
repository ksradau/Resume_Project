from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.resume.models import ResumePage
from apps.resume.models import Technology
from apps.resume.models import Project
from apps.resume.models import Responsibility


@admin.register(ResumePage)
class ResumePageAdminModel(ModelAdmin):
    pass


@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    pass


@admin.register(Project)
class TechnologyAdminModel(ModelAdmin):
    pass


@admin.register(Responsibility)
class TechnologyAdminModel(ModelAdmin):
    pass