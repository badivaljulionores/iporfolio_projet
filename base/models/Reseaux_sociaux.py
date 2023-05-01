from django.db import models
# from .Utilisateur import Utilisateur

# Create your models here.
class Reseaux_sociaux(models.Model):
    name_media_social = models.CharField(max_length=100, verbose_name="nom du réseau")
    link_media_social = models.URLField(verbose_name="lien du réseau")
    # utilisateurs = models.ManyToManyField('Utilisateur', related_name='reseaux', blank=True)


