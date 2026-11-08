from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Matiere, Ressource

# Configuration pour afficher les utilisateurs personnalisés
class CustomUserAdmin(UserAdmin):
    # On ajoute nos champs (role, serie, langue) à la page de modification
    fieldsets = UserAdmin.fieldsets + (
        ('Informations personnalisées', {'fields': ('role', 'serie', 'langue')}),
    )
    # On ajoute le rôle et la série dans la liste des utilisateurs
    list_display = ('username', 'email', 'role', 'serie', 'is_staff')

# On enregistre les modèles
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Matiere)
admin.site.register(Ressource)