from rest_framework import serializers

from ..models.permisos import Coordinador
from ..models.permisos import Miembros
from ..models.permisos import Proyectleader


class ProyectoLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectleader
        fields = '__all__'


class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'


class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembros
        fields = '__all__'
