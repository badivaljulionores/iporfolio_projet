from django.db import models

class UserMetier(models.Model):
    metier = models.ForeignKey('Metier', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)