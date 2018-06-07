from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^templates/download$', views.download, name="download"),
    url(r'^templates/download_by_ver$', views.download_by_ver, name="ver01")
]