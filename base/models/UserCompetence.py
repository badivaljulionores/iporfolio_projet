from django.db import models

# from .Competences import Competences
# from .Utilisateur import Utilisateur

class UserCompetence(models.Model):
    user = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    competence = models.ForeignKey('Competences', on_delete=models.CASCADE)