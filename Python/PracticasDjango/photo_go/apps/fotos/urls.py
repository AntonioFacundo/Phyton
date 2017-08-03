from django.conf.urls import url, include
from apps.fotos.views import index_foto


urlpatterns = [
	url(r'^$', index_foto),

]