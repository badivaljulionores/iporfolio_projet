from django.db import models
# from .Utilisateur import Utilisateur
# from .Projets import Projets
# from .Temoignages import Temoignages
# Create your models here.
class UserProjet(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    projet = models.ForeignKey('Projets', on_delete=models.CASCADE)
    temoignage = models.ManyToManyField('Temoignages', blank=True)

    class Meta:
        unique_together = ('user', 'projet')