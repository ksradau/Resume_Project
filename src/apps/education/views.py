from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_education(request: HttpRequest) -> HttpResponse:
    return render(request, "education/education.html")