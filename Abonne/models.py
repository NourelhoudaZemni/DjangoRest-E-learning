from django.db import models

# Create your models here.
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an email username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

        def Create_superuser(self, email, username, password):
            user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,

            )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user


class TypeAbonn(models.TextChoices):
    Etudiant = 'Et', ('Etudiant')
    Enseignant = 'En', ('Enseignant')
    Admin = 'Admin', ('Administrateur')


class Abonne(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=60, unique=True)
    # date_joined = models.DateTimeField ( verbose_name = "date joined" , auto_now_add = True )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_de_naissance = models.DateField()
    numero_de_tel = models.IntegerField()
    type = models.CharField(max_length=20,
                            choices=TypeAbonn.choices,
                            default=TypeAbonn.Etudiant, )

    USERNAME_FIElD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, prem, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.nom_niveau


class Matiere(models.Model):
    Nom_matiere = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, db_index=True)
    Niveau = models.ForeignKey(Niveau, related_name='matiers', on_delete=models.CASCADE)


class Enseignant(Abonne):
    Niveau = models.ManyToManyField(Niveau)
    Matiere = models.ManyToManyField(Matiere)


class Etudiant(Abonne):
    Niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)


class Chapitre(models.Model):
    titre_chapitre = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, db_index=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)


class Document(models.Model):
    Chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    titre_doc = models.CharField(max_length=255)
    description_doc = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=255, db_index=True)


class Video(models.Model):
    Chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    titre_video = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, db_index=True)
    nb_like = models.IntegerField()
    nb_dislike = models.IntegerField()
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
