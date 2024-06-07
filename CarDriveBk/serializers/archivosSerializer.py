from rest_framework import serializers

from ..models import Usuarios
from ..models.archivos import Archivos
from ..models.etiquetas import RelacionesEtiquetas
from ..models.servicios import Favoritos


class ArchivoSerializer(serializers.ModelSerializer):
    etiquetas = serializers.SerializerMethodField()
    usuario_info = serializers.SerializerMethodField(read_only=True)
    id_usuario = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Usuarios.objects.all(),
    )
    favorito = serializers.SerializerMethodField()

    class Meta:
        model = Archivos
        fields = ['id', 'nombre', 'descripcion', 'terminacion', 'fecha', 'usuario_info', 'id_usuario', 'etiquetas', 'favorito', 'id_apartado']

    def get_etiquetas(self, obj):
        relaciones = RelacionesEtiquetas.objects.filter(id_archivos=obj)
        etiquetas = [{'nombre': rel.id_etiquetas.nombre, 'color': rel.id_etiquetas.color} for rel in relaciones]
        return etiquetas

    def get_usuario_info(self, obj):
        usuario = obj.id_usuario
        return {
            'id': usuario.id,
            'nombre': usuario.get_full_name(),
            'imagen': usuario.imagen.url if usuario.imagen else None,
            'fecha': usuario.fecha
        }

    def get_favorito(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, "user") and request.user.is_authenticated:
            return Favoritos.objects.filter(id_usuario=request.user, id_archivo=obj).exists()
        return False