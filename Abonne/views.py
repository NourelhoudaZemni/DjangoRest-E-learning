from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Niveau
from .models import Matiere
from .models import Chapitre
from .models import Video

from .models import Document
from .Serializer import MatierSerializer
from .Serializer import NiveauSerializer
from .Serializer import VideoSerializer
from .Serializer import ChapterSerializer
from .Serializer import RegistrationSerializer
from .Serializer import DocumentSerializer


# Create your views here.
# ____________________________________

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if not serializer.is_valid():
        data = serializer.errors
    else:
        abonne = serializer.save()
        data['response'] = "successfuly registered a new user"
        data['email'] = abonne.email
        data['username'] = abonne.username
    return Response(data)


# _______________________________________________________________


#  views for niveau .
@api_view(['GET'])
def niveaulist(request):
    niveau = Niveau.objects.all()
    serializer = NiveauSerializer(niveau, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def niveaudetails(request, pk):
    niveau = Niveau.objects.get(id=pk)
    serializer = NiveauSerializer(niveau, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def niveauadd(request):
    serializer = NiveauSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def niveauUpdate(request, pk):
    niveau = Niveau.objects.get(id=pk)
    serializer = NiveauSerializer(niveau, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def niveauDelete(request, pk):
    niveau = Niveau.objects.get(id=pk)
    niveau.delete()
    return Response("okay")


#  views for matiere  .

@api_view(['GET'])
def matierelist(request):
    matiere = Matiere.objects.all()
    serializer = MatierSerializer(matiere, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def matiereCreate(request):
    serializer = MatierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def matiereUpdate(request, pk):
    matiere = Matiere.objects.get(id=pk)
    serializer = MatierSerializer(matiere, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def matiereDelete(request, pk):
    matiere = Matiere.objects.get(id=pk)
    matiere.delete()
    return Response("deleted")


# Chapitre
@api_view(['GET'])
def ChapitreList(request):
    chapitres = Chapitre.objects.all()
    serializer = ChapterSerializer(chapitres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ChapitreDetail(request, pk):
    chapitres = Chapitre.objects.get(id=pk)
    serializer = ChapterSerializer(chapitres, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ChapterCreate(request):
    serializer = ChapterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data
                    )


@api_view(['PUT'])
def ChapterUpdate(request, pk):
    chapitres = Chapitre.objects.get(id=pk)
    serializer = ChapterSerializer(chapitres, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data
                    )


@api_view(['DELETE'])
def ChapterDelete(request, pk):
    chapter = Chapitre.objects.get(id=pk)
    chapter.delete()
    return Response('deleted')


# video now
@api_view(['GET'])
def VideoList(request):
    vid = Video.objects.all()
    serializer = VideoSerializer(vid, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def VideoDetail(request, pk):
    vid = Video.objects.get(id=pk)
    serializer = VideoSerializer(vid, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def VideoCreate(request):
    serializer = VideoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data
                    )


@api_view(['PUT'])
def VideoUpdate(request, pk):
    vid = Video.objects.get(id=pk)
    serializer = VideoSerializer(vid, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data
                    )


@api_view(['DELETE'])
def VideoDelete(request, pk):
    vid = Video.objects.get(id=pk)
    vid.delete()
    return Response('deleted')


# doc now

@api_view(['GET'])
def DocList(request):
    vid = Document.objects.all()
    serializer = DocumentSerializer(vid, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DocDetail(request, pk):
    vid = Document.objects.get(id=pk)
    serializer = DocumentSerializer(vid, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def DocCreate(request):
    serializer = DocumentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data
                    )


@api_view(['PUT'])
def DocUpdate(request, pk):
    vid = Document.objects.get(id=pk)
    serializer = DocumentSerializer(vid, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data
                    )


@api_view(['DELETE'])
def DocDelete(request, pk):
    vid = Document.objects.get(id=pk)
    vid.delete()
    return Response('deleted')
