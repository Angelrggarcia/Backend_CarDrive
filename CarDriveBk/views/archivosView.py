from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.archivos import Archivos
from ..serializers.archivosSerializer import ArchivoSerializer


class ArchivosView(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    serializer_class = ArchivoSerializer
    filter_backends = (filters.SearchFilter,)
    
    @action(detail=False, methods=['get'], url_path='busqueda')
    def busqueda(self, request):
        nombre = request.query_params.get('nombre', None)
        if nombre is None:
            return Response({"detail": "El parámetro 'nombre' es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            archivos = Archivos.objects.filter(nombre__icontains=nombre)
            if archivos.exists():
                serializer = ArchivoSerializer(archivos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "No se encontraron archivos."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error buscando archivos: {str(e)}")
            return Response({"detail": "Error interno del servidor."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)