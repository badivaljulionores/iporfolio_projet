from django.db import models
from .Utilisateur import Utilisateur
# Create your models here.
class Experiences(models.Model):
    nom_experience = models.CharField(verbose_name="expérience")
    annee_debut = models.DateField(required=True)
    annee_fin = models.DateField()
    entreprise = models.CharField(verbose_name="Entreprise")
    ville = models.CharField(verbose_name="Ville")
    contact = models.CharField("Contact")
    description = models.CharField(verbose_name="Description", required=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    


