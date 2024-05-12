from rest_framework import serializers
from ..models.archivos import Archivos

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = '__all__'