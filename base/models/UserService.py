from django.db import models
from .Utilisateur import Utilisateur
from .Services import Services

class UserService(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'service')