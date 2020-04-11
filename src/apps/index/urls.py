from django.urls import path

from apps.index.views import IndexView
from apps.index.apps import IndexConfig

app_name = IndexConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]