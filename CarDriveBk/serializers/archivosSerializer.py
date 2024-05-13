from rest_framework import serializers
from ..models.archivos import Archivos
from ..models.archivos import Etiquetas
from ..models.archivos import Asociar_etiquetas

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = '__all__'

class AsociacionEtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociar_etiquetas
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiquetas
        fields = '__all__'