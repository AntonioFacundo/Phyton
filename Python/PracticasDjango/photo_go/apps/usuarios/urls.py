from django.conf.urls import url, include
from apps.usuarios.views import index_usuario


urlpatterns = [
    url(r'^$', index_usuario),
]
