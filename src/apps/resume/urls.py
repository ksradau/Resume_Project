from django.urls import path

from apps.resume.views import ResumeView

urlpatterns = [
    path('', ResumeView.as_view(), name="resume"),
]