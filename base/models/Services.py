from django.db import models
# Create your models here.
class Services(models.Model):
    nom_service = models.CharField(max_length=100, verbose_name="Service")
    description = models.TextField(max_length=500, verbose_name="description")
    


