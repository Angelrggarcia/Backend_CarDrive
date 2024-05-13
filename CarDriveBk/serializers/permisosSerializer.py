from rest_framework import serializers
from ..models.permisos import Proyectleader
from ..models.permisos import Coordinador
from ..models.permisos import Miembro

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
        model = Miembro
        fields = '__all__'

