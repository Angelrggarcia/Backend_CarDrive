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
        proyecto_id = self.request.query_params.get('id_proyecto', None)
        proyecto_nombre = self.request.query_params.get('nombre_proyecto', None)
        apartado_id = self.request.query_params.get('id_apartado', None)
        apartado_nombre = self.request.query_params.get('nombre_apartado', None)
        etiqueta_nombre = self.request.query_params.get('etiqueta', None)
        fecha_inicio = self.request.query_params.get('fecha_inicio', None)
        fecha_fin = self.request.query_params.get('fecha_fin', None)
        persona = self.request.query_params.get('persona', None)
        # Filtros para proyectos fecha_inicio, fecha_fin, persona 

        if search:
            queryset = queryset.filter(nombre__icontains=search)
        if proyecto_id:
            queryset = queryset.filter(id_proyecto=proyecto_id)
        if proyecto_nombre:
            queryset = queryset.filter(nombre_proyecto=proyecto_nombre)
        if apartado_id:
            queryset = queryset.filter(id_apartado=apartado_id)
        if apartado_nombre:
            queryset = queryset.filter(nombre_apartado=apartado_nombre)
        if etiqueta_nombre:
            queryset = queryset.filter(
                relaciones_etiquetas__id_etiquetas__nombre__icontains=etiqueta_nombre)
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)
        if persona:
            queryset = queryset.filter(nombre_persona=persona)  
            

        return queryset