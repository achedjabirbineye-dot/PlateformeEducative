from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Le modèle Utilisateur personnalisé
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('eleve', 'Élève'),
        ('prof', 'Professeur'),
    ]
    SERIE_CHOICES = [
        ('A4', 'Série A4'),
        ('C', 'Série C'),
        ('D', 'Série D'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='eleve')
    serie = models.CharField(max_length=2, choices=SERIE_CHOICES, blank=True, null=True)
    langue = models.CharField(max_length=2, choices=[('fr', 'Français'), ('ar', 'Arabe')], default='fr')

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

# 2. Le modèle Matière
class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

# 3. Le modèle Ressource
class Ressource(models.Model):
    TYPE_CHOICES = [
        ('annale', 'Annale du Bac'),
        ('exercice', 'Exercice corrigé'),
        ('fiche', 'Fiche de révision'),
    ]
    LANGUE_CHOICES = [
        ('fr', 'Français'),
        ('ar', 'Arabe'),
    ]
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='ressources/')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    type_ressource = models.CharField(max_length=20, choices=TYPE_CHOICES, default='annale')
    langue = models.CharField(max_length=2, choices=LANGUE_CHOICES, default='fr')
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre