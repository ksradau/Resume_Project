from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.api.impl.v1.views import ReminderViewSet
from applications.api.impl.v1.views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet, "user")
router.register("reminder", ReminderViewSet, "reminder")

urlpatterns = [
    path("", include(router.urls)),
]
