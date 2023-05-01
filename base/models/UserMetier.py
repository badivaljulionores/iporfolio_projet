from django.db import models

class UserMetier(models.Model):
    metier = models.ForeignKey('Metier', on_delete=models.CASCADE)
    user = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)