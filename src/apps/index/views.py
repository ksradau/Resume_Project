from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_index(request: HttpRequest) -> HttpResponse:
    return render(request, "index/index.html")