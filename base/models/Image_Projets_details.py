from django.db import models
# from .Projets_details import Projets_details
# Create your models here.
class Image_Projets_details(models.Model):
    url_image = models.URLField()
    projet_detail = models.ForeignKey('Projets_details', on_delete=models.CASCADE)
    
    


