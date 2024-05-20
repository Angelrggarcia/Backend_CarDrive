from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models.apartado import Apartados


class ApartadosSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Apartados
        fields = '__all__'
