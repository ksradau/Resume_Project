from django.urls import path

from apps.education.views import IndexView

from apps.education.apps import EducationConfig

app_name = EducationConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]