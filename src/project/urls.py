from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from pathlib import Path

here = Path(__file__).parent.resolve()


def view(r):
    index = here.parent.parent / "index.html"
    with index.open("r") as f:
        return HttpResponse(f.read())


def view_css_style(r):
    index = here.parent.parent / "css/style.css"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/css")


def view_css_print(r):
    index = here.parent.parent / "css/print.css"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/css")


def view_css_typography(r):
    index = here.parent.parent / "css/typography.css"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/css")


def view_css_reset(r):
    index = here.parent.parent / "css/reset.css"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/css")


def view_photo(rb):
    index = here.parent.parent / "images/J1HxsPhMYG0_2.jpg"
    with index.open("rb") as f:
        return HttpResponse(f.read())


def view_js_jquery(r):
    index = here.parent.parent / "js/jquery-1.4.4.min.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_slider(r):
    index = here.parent.parent / "js/jquery.bxSlider.min.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_vtip(r):
    index = here.parent.parent / "js/vtip.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_cufon(r):
    index = here.parent.parent / "js/cufon-yui.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_Dill(r):
    index = here.parent.parent / "js/DilleniaUPC_400.font.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_Orator(r):
    index = here.parent.parent / "js/Orator_Std_400.font.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_bgpos(r):
    index = here.parent.parent / "js/jquery.bgpos.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_init(r):
    index = here.parent.parent / "js/init.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


def view_js_form(r):
    index = here.parent.parent / "js/jquery.form.js"
    with index.open("r") as f:
        return HttpResponse(f.read(), content_type="text/javascript")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('css/style.css', view_css_style),
    path('css/print.css', view_css_print),
    path('css/typography.css', view_css_typography),
    path('css/reset.css', view_css_reset),
    path('images/J1HxsPhMYG0_2.jpg', view_photo),
    path('js/jquery-1.4.4.min.js', view_js_jquery),
    path('js/jquery.bxSlider.min.js', view_js_slider),
    path('js/vtip.js', view_js_vtip),
    path('js/cufon-yui.js', view_js_cufon),
    path('js/DilleniaUPC_400.font.js', view_js_Dill),
    path('js/Orator_Std_400.font.js', view_js_Orator),
    path('js/jquery.bgpos.js', view_js_bgpos),
    path('js/init.js', view_js_init),
    path('js/jquery.form.js', view_js_form),



]
