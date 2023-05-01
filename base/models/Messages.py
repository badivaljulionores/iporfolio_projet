from django.db import models
# from .Utilisateur import Utilisateur
# Create your models here.
class Messages(models.Model):
    nom_contact = models.CharField(max_length=100, verbose_name="Contact")
    email_contact = models.EmailField(verbose_name="email")
    objet_contact = models.CharField(max_length=100, verbose_name="Object")
    message = models.TextField(verbose_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    
    


