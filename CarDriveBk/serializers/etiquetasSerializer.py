from rest_framework import serializers

from ..models.etiquetas import Etiquetas
from ..models.etiquetas import RelacionesEtiquetas


class RelacionesEtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionesEtiquetas
        fields = '__all__'


class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiquetas
        fields = '__all__'
