from rest_framework import serializers
from .models import Abonne
from .models import Niveau
from .models import Matiere
from .models import Chapitre
from .models import Video
from .models import Document
#______________________________________________________________________

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'} ,read_only=True)

    class Meta:
        model = Abonne
        fields = ['email','username','password','password2','date_de_naissance','numero_de_tel']
        #pour sécurité
        extra_kwargs={
            'password':{'write_only':True}
        }

def save(self):
    abonne= Abonne(
        email=self.validat_data['email'],
        username=self.validat_data['username'],
        date_de_naissance=self.validat_data['date_de_naissance'],
        numero_de_tel=self.validat_data['numero_de_tel'],
    )
    password=self.validat_data['password']
    password2= self.validat_data[ 'password2' ]
    if password!=password2:
        raise serializers.ValidationError('password:Passwords must match')
    abonne.set_password(password)
    abonne.save()
    return abonne
#chnia account?mekch mdeclariha!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!











#____________________________________________________________________
class MatierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'

class NiveauSerializer(serializers.ModelSerializer):
     matiers = MatierSerializer(many=True)

     class Meta :
            model= Niveau
            fields=['nom_niveau','slug','matiers']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


