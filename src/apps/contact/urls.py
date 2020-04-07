from django.urls import path

from apps.contact.views import view_contact

urlpatterns = [
    path('', view_contact, name="contact"),
]