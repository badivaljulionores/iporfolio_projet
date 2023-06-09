from django.db import models
from .Utilisateur import Utilisateur
from .Projets import Projets
from .Temoignages import Temognages
# Create your models here.
class UserProjet(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)
    temoignage = models.ManyToManyField(Temognages, blank=True)

    class Meta:
        unique_together = ('user', 'projet')