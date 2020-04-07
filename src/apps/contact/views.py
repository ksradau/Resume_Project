from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact/contact.html")