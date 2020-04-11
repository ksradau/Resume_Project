from django.urls import path

from apps.resume.views import IndexView
from apps.resume.apps import ResumeConfig

app_name = ResumeConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]