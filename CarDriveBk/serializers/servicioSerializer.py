from rest_framework import serializers

from .archivosSerializer import ArchivoSerializer
from ..models.servicios import Favoritos
from ..models.servicios import Recientes


class RecienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recientes
        fields = '__all__'


class FavoritoSerializer(serializers.ModelSerializer):
    archivo = ArchivoSerializer(source='id_archivo', read_only=True)  # Nota el uso de 'source'

    class Meta:
        model = Favoritos
        fields = ['archivo']
