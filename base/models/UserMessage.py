from django.db import models
# from .Utilisateur import Utilisateur
# from .Messages import Messages

class UserMessage(models.Model):
    user = models.OneToOneField('Utilisateur', on_delete=models.CASCADE)
    message = models.ForeignKey('Messages', on_delete=models.CASCADE)