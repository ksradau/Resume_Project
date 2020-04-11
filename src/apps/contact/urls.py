from django.urls import path

from apps.contact.views import IndexView
from apps.contact.apps import ContactConfig

app_name = ContactConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]