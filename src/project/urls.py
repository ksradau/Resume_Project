from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import admin
from django.urls import path, re_path
from pathlib import Path
from django.conf import settings
from django.shortcuts import render


STATIC_DIR = settings.PROJECT_DIR / "static"


def view_index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


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
    path('', view_index, name="index"),
    path('resume/', view_resume, name="resume"),
    path('education/', view_education, name="education"),
    path('contact/', view_contact, name="contact"),

]