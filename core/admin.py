from django.contrib import admin
from .models import Matiere, Ressource

# On enregistre les modèles pour qu'ils apparaissent dans l'admin
admin.site.register(Matiere)
admin.site.register(Ressource)