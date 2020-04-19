from django.views.generic import TemplateView

from apps.resume.models import ResumePage


class IndexView(TemplateView):
    template_name = "resume/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = ResumePage.objects.first()
        ctx = {"title": info.title,
               "description": info.description,
               "h1": info.h1,
               "preview": info.preview,
               "article": info.article,
               "text": info.text,
               }

        ctx.update(parent_ctx)

        return ctx