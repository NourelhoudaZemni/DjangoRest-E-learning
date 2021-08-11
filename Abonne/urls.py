from django.contrib import admin
from django.urls import path
from . import views

from Abonne.views import registration_view

urlpatterns = [

    path('niveaulist/', views.niveaulist, name="niveaulist"),
    path('niveaudetails/<int:pk>', views.niveaudetails, name="niveaudetails"),
    path('niveauadd/', views.niveauadd, name="niveauadd"),
    path('niveauUpdate/<int:pk>', views.niveauUpdate, name="niveauUpdate"),
    path('niveauDelete/<int:pk>', views.niveauDelete, name="niveauDelete"),

    # url matiere
    path('matierelist/', views.matierelist, name="matierelist"),
    path('matiereadd/', views.matiereCreate, name="matiereadd"),
    path('matiereUpdate/<int:pk>', views.matiereUpdate, name="matiereUpdate"),
    path('matiereDelete/<int:pk>', views.matiereDelete, name="matiereDelete"),

    # url chapitre
    path('listChapter/', views.ChapitreList, name="chapitres"),
    path('detailChapter/<str:pk>/', views.ChapitreDetail, name="details"),
    path('createChapter/', views.ChapterCreate, name="create"),
    path('updateChapter/<str:pk>/', views.ChapterUpdate, name="update"),
    path('deleteChapter/<str:pk>/', views.ChapterDelete, name="delete"),

    # url video
    path('listVideo/', views.VideoList, name="ListedVideo"),
    path('detailVideo/<str:pk>/', views.VideoDetail, name="detailsV"),
    path('createVideo/', views.VideoCreate, name="createV"),
    path('updateVideo/<str:pk>/', views.VideoUpdate, name="updateV"),
    path('deleteVideo/<str:pk>/', views.VideoDelete, name="deleteV"),

    # doc url
    path('listDoc/', views.DocList, name="ListedVideo"),
    path('detailDoc/<str:pk>/', views.DocDetail, name="detailsV"),
    path('createDoc/', views.DocCreate, name="createV"),
    path('updateDoc/<str:pk>/', views.DocUpdate, name="updateV"),
    path('deleteDoc/<str:pk>/', views.DocDelete, name="deleteV"),

    # register
    path('register/', registration_view, name="register")
]
