from django.db import models
# from .Utilisateur import Utilisateur
# Create your models here.
class Formations(models.Model):
    nom_formation = models.CharField(max_length=100, verbose_name="formation")
    annee_debut = models.DateField(null=False, blank=False)
    annee_fin = models.DateField()
    etablissement = models.CharField(max_length=100, verbose_name="Etablissement")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    description = models.CharField(max_length=500, verbose_name="Description")
    user = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    


