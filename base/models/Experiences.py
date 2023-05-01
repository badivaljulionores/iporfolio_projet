from django.db import models
# from .Utilisateur import Utilisateur
# Create your models here.
class Experiences(models.Model):
    nom_experience = models.CharField(max_length=100, verbose_name="expérience")
    annee_debut = models.DateField(null=False, blank=False)
    annee_fin = models.DateField()
    entreprise = models.CharField(max_length=100, verbose_name="Entreprise")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    contact = models.CharField(max_length=100, verbose_name="Contact")
    description = models.CharField(max_length=500, verbose_name="Description", null=False, blank=False)
    user = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    


