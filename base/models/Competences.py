from django.db import models
# Create your models here.
class Competences(models.Model):
    nom_competence = models.CharField()
    niveau_competence = models.DecimalField(max_digits=5, decimal_places=2)