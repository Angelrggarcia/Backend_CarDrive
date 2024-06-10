from rest_framework import serializers
from django.db.models import Max


from ..models import Usuarios
from ..models.archivos import Archivos
from ..models.etiquetas import RelacionesEtiquetas, Etiquetas
from ..models.servicios import Favoritos
from ..models.versiones import Versiones


class ArchivoSerializer(serializers.ModelSerializer):
    etiquetas = serializers.SerializerMethodField()
    iteracion = serializers.SerializerMethodField()
    usuario_info = serializers.SerializerMethodField(read_only=True)
    
    id_usuario = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Usuarios.objects.all(),
    )
    favorito = serializers.SerializerMethodField()

    class Meta:
        model = Archivos
        fields = ['id', 'nombre', 'descripcion', 'terminacion', 'fecha', 'usuario_info', 'id_usuario', 'etiquetas', 'favorito', 'id_apartado', 'iteracion']

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

    def get_usuario_info(self, obj):
        usuario = obj.id_usuario
        return {
            'id': usuario.id,
            'nombre': usuario.get_full_name(),
            'color': usuario.color,
            'imagen': usuario.imagen.url if usuario.imagen else None,
            'fecha': usuario.fecha
        }

    def get_favorito(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, "user") and request.user.is_authenticated:
            return Favoritos.objects.filter(id_usuario=request.user, id_archivo=obj).exists()
        return False

    def create(self, validated_data):
        etiquetas_data = validated_data.pop('etiquetas', [])  # Usa .get() para evitar KeyError
        archivo = Archivos.objects.create(**{k: v for k, v in validated_data.items() if k not in ['etiquetas']})

        for etiqueta_data in etiquetas_data:
            etiqueta, created = Etiquetas.objects.get_or_create(
                nombre=etiqueta_data['nombre'],
                defaults={'color': etiqueta_data.get('color', 'default_color')}
            )
            RelacionesEtiquetas.objects.create(id_archivos=archivo, id_etiquetas=etiqueta)

        return archivo