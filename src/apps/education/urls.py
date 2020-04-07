from django.urls import path

from apps.education.views import view_education

urlpatterns = [
    path('', view_education, name="education"),
]