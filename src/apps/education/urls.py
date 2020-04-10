from django.urls import path

from apps.education.views import EdView

urlpatterns = [
    path('', EdView.as_view(), name="education"),
]