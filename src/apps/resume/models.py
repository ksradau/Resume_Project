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


class Technology(m.Model):
    name = m.TextField()
    description = m.TextField(null=True, blank=True)


class Project(m.Model):
    started_at = m.DateField(null=True, blank=True)
    finished_at = m.DateField(null=True, blank=True)
    summary = m.TextField(null=True, blank=True)
    technologies = m.ManyToManyField(Technology, related_name="project")


class Responsibility(m.Model):
    summary = m.TextField()
    project = m.ForeignKey(Project, on_delete=m.CASCADE, related_name="responsibilities")

