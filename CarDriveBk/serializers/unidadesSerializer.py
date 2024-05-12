from rest_framework import serializers
from ..models import Apartado

class ApartadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartado
        fields = '__all__'