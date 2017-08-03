from django.conf.urls import url, include
from apps.adopcion.views import index_ado


urlpatterns = [
    url(r'^index$', index_ado),
]
