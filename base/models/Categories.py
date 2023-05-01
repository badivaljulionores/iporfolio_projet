from django.db import models
from .Projets import Projets
# Create your models here.
class Categories(models.Model):
    categorie = models.CharField(max_length=100, verbose_name="Catgéorie")

    
    
    


