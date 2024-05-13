from rest_framework import serializers
from ..models.proyectos import Proyecto, Archivados

class  ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class  ArchivadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivados
        fields = '__all__'