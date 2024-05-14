from rest_framework import serializers
from ..models.etiquetas import Etiquetas
from ..models.etiquetas import Asociar_etiquetas

class AsociacionEtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociar_etiquetas
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiquetas
        fields = '__all__'