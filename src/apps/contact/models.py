from django.db import models as m


class ContactPage(m.Model):
    title = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    h1 = m.TextField(null=True, blank=True)
    information = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Page"

    def __str__(self):
        return f"ContactPage(id={self.pk})"