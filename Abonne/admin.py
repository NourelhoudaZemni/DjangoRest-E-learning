from django.contrib import admin

# Register your models here.
from Abonne.models import *

admin.site.register(Enseignant)
admin.site.register(Abonne)
admin.site.register(Etudiant)
admin.site.register(Matiere)
admin.site.register(Chapitre)
admin.site.register(Video)
admin.site.register(Document)
admin.site.register(Niveau)
