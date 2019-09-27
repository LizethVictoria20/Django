from django.conf.urls import url, include

from zoo.views import ContinenteList, ContinenteCreate, ContinenteUpdate, ContinenteDelete
from zoo.views import HabitatCreate, HabitatList, HabitatUpdate, HabitatDelete

urlpatterns = [
	url(r'^listar$', ContinenteList.as_view(), name = 'continente_listar'),
	url(r'^nuevo$', ContinenteCreate.as_view(), name = 'continente_nuevo'),
	url(r'^editar/(?P<pk>[\w]+)$', ContinenteUpdate.as_view(), name = 'continente_editar'),
	url(r'^eliminar/(?P<pk>[\w]+)$', ContinenteDelete.as_view(), name = 'continente_eliminar'),

	url(r'^hab_nuevo$', HabitatCreate.as_view(), name = 'habitat_nuevo'),
	url(r'^hab_listar$', HabitatList.as_view(), name = 'habitat_listar'),
	url(r'^hab_editar/(?P<pk>[\w]+)$', HabitatUpdate.as_view(), name = 'habitat_editar'),
	url(r'^hab_eliminar/(?P<pk>[\w]+)$', HabitatDelete.as_view(), name = 'habitat_eliminar'),

]