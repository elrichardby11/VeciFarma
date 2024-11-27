from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("descargar/", views.download, name="download"),
    path("solicitud/", include("requests.urls"))
]
