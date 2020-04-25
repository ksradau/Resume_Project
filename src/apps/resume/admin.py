from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.resume.models import ResumePage
from apps.resume.models import Technology
from apps.resume.models import Project
from apps.resume.models import Responsibility



from functools import singledispatch
from typing import Text

import django
from django.db.models.base import ModelBase
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.db.models.fields.related_descriptors import ManyToManyDescriptor
from django.db.models.query_utils import DeferredAttribute

from typing import Iterable
from django import forms
from django.db import models


@singledispatch
def a(obj) -> Text:
    return str(obj)


@a.register
def _(obj: DeferredAttribute) -> Text:
    if django.VERSION[0] < 3:  # pragma: nocover
        return obj.field_name
    return obj.field.get_attname()


@a.register
def _(obj: ForwardManyToOneDescriptor) -> Text:
    return obj.field.name


@a.register
def _(obj: ManyToManyDescriptor) -> Text:
    return obj.field.name


@a.register
def _(obj: ModelBase) -> Text:
    return obj._meta.db_table


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