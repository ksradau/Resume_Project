from django.views.generic import TemplateView
from apps.contact.models import ContactPage


class IndexView(TemplateView):
    template_name = "contact/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)

        info = ContactPage.objects.first()
        ctx = {"title": info.title,
               "description": info.description,
               "h1": info.h1,
               "information": info.information,
               }

        ctx.update(parent_ctx)

        return ctx