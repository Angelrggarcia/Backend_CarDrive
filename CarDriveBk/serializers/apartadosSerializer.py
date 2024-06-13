from rest_framework import serializers

from ..models.apartado import Apartados
from drf_extra_fields.fields import Base64ImageField

class ApartadoSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Apartados
        fields = '__all__'
