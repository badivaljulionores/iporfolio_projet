from django.db import models
from .Projets import Projets
from .Categories import Categories
# Create your models here.
class Projets_details(models.Model):
    date_projet = models.DateField()
    clients = models.CharField(verbose_name='Clients')
    depot_projet = models.CharField()
    url_projet = models.URLField()
    description = models.TextField()
    projet = models.ForeignKey(Projets)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    
    


