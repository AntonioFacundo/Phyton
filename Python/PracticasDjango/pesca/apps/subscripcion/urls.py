from django.conf.urls import url, include
from apps.subscripcion.views import index


urlpatterns = [
    url(r'^$', index),
]