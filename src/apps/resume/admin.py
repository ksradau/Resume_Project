from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.resume.models import ResumePage
from apps.resume.models import Technology
from apps.resume.models import Project
from apps.resume.models import Responsibility




from typing import Iterable
from django import forms
from django.db import models


def a(obj):
    return obj.field.name


def gen_textinput_admin_form(
    model_cls: type, model_fields: Iterable[models.Field]
) -> type:
    model_field_names = (a(_field) for _field in model_fields)

    class AdminFormWithTextInputs(forms.ModelForm):
        class Meta:
            model = model_cls
            fields = "__all__"
            widgets = {
                _field: forms.TextInput(attrs={"size": "100"})
                for _field in model_field_names
            }

    return AdminFormWithTextInputs







@admin.register(ResumePage)
class ResumePageAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        ResumePage, (ResumePage.title, ResumePage.h1, ResumePage.preview)
    )


@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Technology, (Technology.name, Technology.description)
    )


@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Project, (Project.link, Project.name)
    )


@admin.register(Responsibility)
class ResponsibilityAdminModel(ModelAdmin):
    pass