from django.db import models

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Ressource(models.Model):
    # Choix possibles pour le type de document
    TYPE_CHOICES = [
        ('annale', 'Annale du Bac'),
        ('exercice', 'Exercice corrigé'),
        ('fiche', 'Fiche de révision'),
    ]
    
    # Choix possibles pour la langue
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