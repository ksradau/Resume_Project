from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from pathlib import Path

here = Path(__file__).parent.resolve()


def view(r):
    return read_static("index.html", "text/html")


def view_css_style(r):
    return read_static("css/style.css", "text/css")


def view_css_print(r):
    return read_static("css/print.css", "text/css")


def view_css_typography(r):
    return read_static("css/typography.css", "text/css")


def view_css_reset(r):
    return read_static("css/reset.css", "text/css")


def view_js_jquery(r):
    return read_static("js/jquery-1.4.4.min.js", "text/javascript")


def view_js_slider(r):
    return read_static("js/jquery.bxSlider.min.js", "text/javascript")


def view_js_vtip(r):
    return read_static("js/vtip.js", "text/javascript")


def view_js_cufon(r):
    return read_static("js/cufon-yui.js", "text/javascript")


def view_js_Dill(r):
    return read_static("js/DilleniaUPC_400.font.js", "text/javascript")


def view_js_Orator(r):
    return read_static("js/Orator_Std_400.font.js", "text/javascript")


def view_js_bgpos(r):
    return read_static("js/jquery.bgpos.js", "text/javascript")


def view_js_init(r):
    return read_static("js/init.js", "text/javascript")


def view_js_form(r):
    return read_static("js/jquery.form.js", "text/javascript")


def view_photo(rb):
    return read_static("images/J1HxsPhMYG0_2.jpg", "image/jpeg", "rb")


def read_static(stat_url, content, method="r"):
    index = here.parent.parent / stat_url
    with index.open(method) as f:
        return HttpResponse(f.read(), content_type=content)


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
