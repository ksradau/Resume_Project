from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import render

from apps.index.views import view_index

STATIC_DIR = settings.PROJECT_DIR / "static"


def view_resume(request: HttpRequest) -> HttpResponse:
    return render(request, "resume.html")


def view_education(request: HttpRequest) -> HttpResponse:
    return render(request, "education.html")


def view_contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


"""def view_css(request: HttpRequest) -> HttpResponse:
    return render_static(request, "text/css")


def render_static(file_path: Path, content_type: str) -> HttpResponse:
    with file_path.open("rb") as fp:
        content = fp.read()
    response = HttpResponse(content, content_type=content_type)
    return response
"""


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("apps.index.urls")),

    path('resume/', view_resume, name="resume"),
    path('education/', view_education, name="education"),
    path('contact/', view_contact, name="contact"),

]