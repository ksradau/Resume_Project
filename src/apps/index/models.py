from django.db import models as m


class UserInfo(m.Model):
    name = m.TextField(unique=True)
    greeting = m.TextField(null=True, blank=True)
    age = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "User Info"

    def __str__(self):
        return f"UserInfo(id={self.pk}, name={self.name!r})"
