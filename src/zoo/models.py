from django.db import models

# Create your models here.
class Continente(models.Model):
	nombre = models.CharField(max_length=15, unique=True)

	def __str__(self):
		return '{}'.format(self.nombre)



class Habitat(models.Model):
	id_hab = models.CharField(max_length=8, primary_key=True)
	nombre = models.CharField(max_length=20, unique=True)
	clima = models.CharField(max_length=20, unique=True)
	vegetacion = models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.nombre)


class HabitatContinente(models.Model):
	continente = models.ForeignKey(Continente, null=True, blank=True, on_delete= models.CASCADE)
	habitat = models.ForeignKey(Habitat, null=True, blank=True, on_delete= models.CASCADE)


	def __str__(self):
		return '{}{}{}'.format(self.id, self.continente, self.habitat)