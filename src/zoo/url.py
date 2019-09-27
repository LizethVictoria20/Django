from django.conf.urls import url, include

from zoo.views import ContinenteList

urlpatterns=[
	url(r'^listar$', ContinenteList.as_views(), name='continente_listar'),
	
]