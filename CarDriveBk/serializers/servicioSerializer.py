from rest_framework import serializers
from ..models.servicios import Favoritos
from ..models.servicios import Recientes

class RecienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recientes
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'