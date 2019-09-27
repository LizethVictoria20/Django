from django.contrib import admin

# Register your models here.
from zoo.models import Continente, Habitat, HabitatContinente



admin.site.register(Continente)
admin.site.register(Habitat)
admin.site.register(HabitatContinente)