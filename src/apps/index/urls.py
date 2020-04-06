from django.urls import path

from apps.index.views import view_index

urlpatterns = [
    path('', view_index, name="index"),
]