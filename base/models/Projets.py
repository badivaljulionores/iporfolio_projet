from django.db import models
from gdstorage.storage import GoogleDriveStorage
from decouple import config
# Create your models here.
class Projets(models.Model):
    CHOICES = [('personnel', 'PERSONNEL'), ('collaboratif', 'COLLABORATIF')]
    nom_projet = models.CharField(verbose_name="projet")
    personnel_collaboratif = models.CharField(choices=CHOICES, verbose_name='personnel ou collaboratif ?')
    clients_satisfaits = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
        
    def storage():
        storage = None
        if config('ENV') == 'PRODUCTION':
            gd_storage = GoogleDriveStorage()
            storage = gd_storage
        return storage
    
    image = models.ImageField(verbose_name='Image', null=True, blank=True, storage=storage())
    
    
    


