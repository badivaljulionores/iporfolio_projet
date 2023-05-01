from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from gdstorage.storage import GoogleDriveStorage
from decouple import config

#Importation des modeles
from .Competences import Competences
from .Metier import Metier
from .Reseaux_sociaux import Reseaux_sociaux
from .Services import Services
from .UserCompetence import UserCompetence
from .UserService import UserService
from .Messages import Messages
from .UserMessage import UserMessage
# Create your models.

class Utilisateur(AbstractUser):
    first_name = models.CharField(max_length=128, verbose_name='prénom')
    last_name = models.CharField(max_length=128, verbose_name='nom')
    telephone = models.CharField(verbose_name='téléphone')
    active = models.BooleanField(default=True)
    bloque = models.BooleanField(default=False)
    date_birth = models.DateField(verbose_name = "date de naissance",null=True, blank=True)
    level_academic = models.CharField()
    ville = models.CharField()
    resume = models.TextField()
    petite_biographie_1 = models.TextField()
    petite_biographie_2 = models.TextField()
    localisation_adresse = models.CharField("Zone géographique")
    localisation_lattitude = models.IntegerField(default=0)
    localisation_longitude = models.IntegerField(default=0)
    
    def storage():
        storage = None
        if config('ENV') == 'PRODUCTION':
            gd_storage = GoogleDriveStorage()
            storage = gd_storage
        return storage
    profile_photo = models.ImageField(verbose_name='photo de profil', null=True, blank=True, storage=storage())
    
    #Clé Secondaire
    competences = models.ManyToManyField(Competences, through=UserCompetence)
    metiers = models.ManyToManyField(Metier, blank=True)
    reseaux = models.ManyToManyField(Reseaux_sociaux, related_name='utilisateurs', blank=True)
    services = models.ManyToManyField(Services, through=UserService)
    messages = models.ManyToManyField(Messages, through=UserMessage)
    
    
    
    
