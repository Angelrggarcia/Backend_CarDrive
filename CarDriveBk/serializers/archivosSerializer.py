from rest_framework import serializers
from django.db.models import Max


from ..models import Usuarios
from ..models.archivos import Archivos
from ..models.etiquetas import RelacionesEtiquetas
from ..models.servicios import Favoritos
from ..models.versiones import Versiones


class ArchivoSerializer(serializers.ModelSerializer):
    etiquetas = serializers.SerializerMethodField()
    iteracion = serializers.SerializerMethodField()
    propietario = serializers.SerializerMethodField(read_only=True)
    id_usuario = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Usuarios.objects.all(),
    )
    favorito = serializers.SerializerMethodField()

    class Meta:
        model = Archivos

        fields = ['id', 'nombre', 'descripcion', 'terminacion', 'fecha', 'propietario', 'id_usuario', 'etiquetas', 'favorito', 'id_apartado', 'iteracion']

    def get_etiquetas(self, obj):
        relaciones = RelacionesEtiquetas.objects.filter(id_archivos=obj)
        etiquetas = [{'nombre': rel.id_etiquetas.nombre, 'color': rel.id_etiquetas.color} for rel in relaciones]
        return etiquetas
    
    def get_iteracion(self, obj):
        busqueda = Versiones.objects.filter(id_archivo=obj)
        resultado = busqueda.aggregate(Max('iteracion'))
        iteracion_max = resultado['iteracion__max']
        
        if iteracion_max is None:
            iteracion_max = 0
    
        return  iteracion_max

    def get_propietario(self, obj):
        usuario = obj.id_usuario
        return {
            'id': usuario.id,
            'primer_nombre': usuario.first_name,
            'segundo_nombre': usuario.last_name,
            'color': usuario.color,
            'imagen': usuario.imagen.url if usuario.imagen else None,
            'fecha': usuario.fecha
        }

    def get_favorito(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, "user") and request.user.is_authenticated:
            return Favoritos.objects.filter(id_usuario=request.user, id_archivo=obj).exists()
        return False