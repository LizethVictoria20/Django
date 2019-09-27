from django import forms

from zoo.models import Continente, Habitat

class ContinenteForm(forms.ModelForm):

	class Meta:
		model= Continente


		fields = [
			'nombre',

		]
		labels = {

			'nombre': 'Nombre',

		}

		widgets = {

			'nombre': forms.TextInput(attrs = {'class':'form-control'})

		}


class HabitatForm(forms.ModelForm):
	class Meta:
		model = Habitat

		fields = [
			'id_hab',
			'nombre',
			'clima',
			'vegetacion'

		]

		labels = {
			'id_hab' : 'Id Habitat',
			'nombre' : 'Nombre',
			'clima' : 'Clima',
			'vegetacion' : 'Vegetacion '
		}

		widgets = {
			'id_hab': forms.TextInput(attrs = {'class':'form-control'}),
			'nombre': forms.TextInput(attrs = {'class':'form-control'}),
			'clima': forms.TextInput(attrs = {'class':'form-control'}),
			'vegetacion': forms.TextInput(attrs = {'class':'form-control'})
		}
