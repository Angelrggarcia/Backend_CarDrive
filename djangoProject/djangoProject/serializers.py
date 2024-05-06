from rest_framework import serializers
from proyectos.models import proyectos
from unidades.models import unidades
from archivos.models import archivos
from archivos.models import carpetas


class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = proyectos
        fields = '__all__'

class UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = unidades
        fields = '_all_'
        
class ArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = archivos
        fields = '__all__'

class CarpetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = carpetas
        fields = '__all__'
    
        