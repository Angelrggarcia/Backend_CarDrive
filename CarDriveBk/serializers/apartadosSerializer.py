from rest_framework import serializers

from ..models.apartado import Apartados


class ApartadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartados
        fields = '__all__'
