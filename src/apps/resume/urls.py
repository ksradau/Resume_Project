from django.urls import path

from apps.resume.views import view_resume

urlpatterns = [
    path('', view_resume, name="resume"),
]