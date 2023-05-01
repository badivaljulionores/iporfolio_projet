from django.db import models
from .Utilisateur import Utilisateur
# Create your models here.
class Formations(models.Model):
    nom_formation = models.CharField(verbose_name="formation")
    annee_debut = models.DateField(required=True)
    annee_fin = models.DateField()
    etablissement = models.CharField(verbose_name="Etablissement")
    ville = models.CharField(verbose_name="Ville")
    description = models.CharField(verbose_name="Description")
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    


