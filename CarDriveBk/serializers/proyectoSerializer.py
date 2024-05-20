from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models.proyectos import Proyectos


class ProyectoSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Proyectos
        fields = '__all__'

