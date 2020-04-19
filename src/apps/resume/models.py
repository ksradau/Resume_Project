from django.db import models as m


class ResumePage(m.Model):
    title = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    h1 = m.TextField(null=True, blank=True)
    preview = m.TextField(null=True, blank=True)
    article = m.TextField(null=True, blank=True)
    text = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Resume Page"

    def __str__(self):
        return f"ResumePage(id={self.pk})"
