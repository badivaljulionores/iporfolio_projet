from django.db import models
# Create your models here.
class Services(models.Model):
    nom_service = models.CharField(verbose_name="Service")
    description = models.TextField(verbose_name="description")
    


