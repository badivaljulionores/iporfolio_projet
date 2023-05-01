from django.contrib import admin

# Register your models here.
from base.models.Categories import Categories
from base.models.Competences import Competences
from base.models.Experiences import Experiences
from base.models.Formations import Formations
from base.models.Image_Projets_details import Image_Projets_details
from base.models.Messages import Messages
from base.models.Metier import Metier
from base.models.Projets_details import Projets_details
from base.models.Projets import Projets
from base.models.Reseaux_sociaux import Reseaux_sociaux
from base.models.Services import Services
from base.models.Temoignages import Temoignages
from base.models.UserCompetence import UserCompetence
from base.models.UserMessage import UserMessage
from base.models.UserMetier import UserMetier
from base.models.UserProjet import UserProjet
from base.models.UserService import UserService
from base.models.Utilisateur import Utilisateur


admin.site.register(Categories)
admin.site.register(Competences)
admin.site.register(Experiences)
admin.site.register(Formations)
admin.site.register(Image_Projets_details)
admin.site.register(Messages)
admin.site.register(Metier)
admin.site.register(Projets_details)
admin.site.register(Projets)
admin.site.register(Reseaux_sociaux)
admin.site.register(Services)
admin.site.register(Temoignages)
admin.site.register(UserCompetence)
admin.site.register(UserMessage)
admin.site.register(UserMetier)
admin.site.register(UserProjet)
admin.site.register(UserService)
admin.site.register(Utilisateur)
