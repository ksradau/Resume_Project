from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.contact.models import ContactPage


@admin.register(ContactPage)
class ContactPageAdminModel(ModelAdmin):
    pass