from django.conf.urls import url, include
from apps.inventario.views import index_inv


urlpatterns = [
    url(r'^$', index_inv),
]