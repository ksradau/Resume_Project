from django.contrib import admin
from django.urls import path, include
from django.conf import settings

STATIC_DIR = settings.PROJECT_DIR / "static"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('resume/', include("apps.resume.urls")),
    path('education/', include("apps.education.urls")),
    path('contact/', include("apps.contact.urls")),

]