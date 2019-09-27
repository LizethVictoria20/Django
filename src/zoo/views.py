from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from zoo.models import Continente, Habitat
from zoo.forms import ContinenteForm, HabitatForm


# Create your views here.

class ContinenteList(ListView):
	model = Continente
	template_name = 'continente_list.html'

class ContinenteCreate(CreateView):
	model = Continente
	form_class = ContinenteForm
	template_name = 'continente_form.html'
	success_url = reverse_lazy('zoo:continente_listar')

class ContinenteUpdate(UpdateView):
	model = Continente
	form_class = ContinenteForm
	template_name = 'continente_form.html'
	success_url = reverse_lazy('zoo:continente_listar')

class ContinenteDelete(DeleteView):
	model = Continente
	template_name = 'continente_delete.html'
	success_url = reverse_lazy('zoo:continente_listar')


class HabitatCreate(CreateView):
	model = Habitat
	form_class = HabitatForm
	template_name = 'habitat_form.html'
	success_url = reverse_lazy('zoo:habitat_listar')

class HabitatList(ListView):
	model = Habitat
	template_name = 'habitat_list.html'
	
class HabitatUpdate(UpdateView):
	model = Habitat
	form_class = HabitatForm
	template_name = 'habitat_form.html'
	success_url = reverse_lazy('zoo:habitat_listar')

class HabitatDelete(DeleteView):
	model = Habitat
	template_name = 'habitat_delete.html'
	success_url = reverse_lazy('zoo:habitat_listar')

