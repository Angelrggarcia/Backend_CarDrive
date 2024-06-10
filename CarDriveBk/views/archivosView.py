from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from ..models.archivos import Archivos
from ..models.servicios import Favoritos
from ..serializers.archivosSerializer import ArchivoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action

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
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def recientes(self, request, format=None):
        user = request.user
        latest_files = Archivos.objects.filter(id_usuario=user).order_by('-fecha')[:15]
        serializer = ArchivoSerializer(latest_files, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def favoritos(self, request, format=None):
        user = request.user
        # if user.is_anonymous:
        #     return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        favoritos_ids = Favoritos.objects.filter(id_usuario=user).values_list('id_archivo', flat=True)
        archivos_favoritos = Archivos.objects.filter(id__in=favoritos_ids)
        serializer = ArchivoSerializer(archivos_favoritos, many=True, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def toggle_favorito(self, request, format=None):
        user = request.user  # Obtener el usuario autenticado
        id_archivo = request.data.get('id_archivo')  # Corregir la obtención del id_archivo
        if not id_archivo:
            return Response({'detail': 'id_archivo es requerido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            archivo = Archivos.objects.get(id=id_archivo)
        except Archivos.DoesNotExist:
            return Response({'detail': 'Archivo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        favorito, created = Favoritos.objects.get_or_create(id_usuario=user, id_archivo=archivo)
        
        if not created:
            favorito.delete()
            return Response({'favorito': False}, status=status.HTTP_200_OK)
        
        return Response({'favorito': True}, status=status.HTTP_201_CREATED)