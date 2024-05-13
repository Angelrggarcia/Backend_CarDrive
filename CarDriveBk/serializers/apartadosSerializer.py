from rest_framework import serializers
from ..models.apartado import Apartado

class ApartadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartado
        fields = '__all__'