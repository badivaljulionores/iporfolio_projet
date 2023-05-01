from django.db import models
from .Projets import Projets
# from .Categories import Categories
# Create your models here.
class Projets_details(models.Model):
    date_projet = models.DateField()
    clients = models.CharField(max_length=100, verbose_name='Clients')
    depot_projet = models.CharField(max_length=100)
    url_projet = models.URLField()
    description = models.TextField(max_length=500)
    # projet = models.ForeignKey(Projets)
    categorie = models.ForeignKey('Categories', on_delete=models.CASCADE)
    
    
    


