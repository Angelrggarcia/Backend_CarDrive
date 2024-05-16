from rest_framework import serializers

from ..models.apartado import Apartados


class ApartadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartados
        fields = '__all__'
