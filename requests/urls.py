from django.urls import path

from . import views

urlpatterns = [
    path("", views.job_request, name="job_request"),
]
