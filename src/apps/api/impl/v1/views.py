from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from applications.api.impl.v1.serializers import ReminderSerializer
from applications.api.impl.v1.serializers import UserSerializer
from applications.reminders.models import Reminder

User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReminderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReminderSerializer

    def get_queryset(self):
        criteria = Q(creator=self.request.user) | Q(
            participants__in=[self.request.user]
        )
        return Reminder.objects.filter(criteria)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
