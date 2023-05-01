from django.db import models

# Create your models here.
class Metier(models.Model):
    name_work = models.CharField(verbose_name="nom du métier")
    


