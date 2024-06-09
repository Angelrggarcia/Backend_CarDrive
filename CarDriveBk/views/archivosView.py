from rest_framework import viewsets, filters, status
from ..models.archivos import Archivos
from ..serializers.archivosSerializer import ArchivoSerializer

# api/archivos/?search=nombre_del_archivo&id_apartado=valor_del_id_apartado&etiqueta=nombre_de_etiqueta
class ArchivosView(viewsets.ModelViewSet):
    queryset = Archivos.objects.prefetch_related('relaciones_etiquetas').all()
    serializer_class = ArchivoSerializer
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        apartado_id = self.request.query_params.get('id_apartado', None)
        etiqueta_nombre = self.request.query_params.get('etiqueta', None)

        if search:
            queryset = queryset.filter(nombre__icontains=search)
        if apartado_id:
            queryset = queryset.filter(id_apartado=apartado_id)
        if etiqueta_nombre:
            queryset = queryset.filter(
                relaciones_etiquetas__id_etiquetas__nombre__icontains=etiqueta_nombre
            )

        return queryset