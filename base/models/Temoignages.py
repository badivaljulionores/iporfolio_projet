from django.db import models
# Create your models here.
class Temoignages(models.Model):
    nom_client = models.CharField(verbose_name="Client")
    metier_client = models.CharField(verbose_name="Metier")
    message_client = models.TextField(verbose_name="Message")
    url_image = models.URLField(verbose_name="Url de l'image")
    
    
    


