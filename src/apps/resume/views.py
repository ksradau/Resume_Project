from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "resume/index.html"