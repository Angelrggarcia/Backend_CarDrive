from rest_framework import viewsets, filters
from rest_framework.response import Response

from ..models.servicios import Recientes, Favoritos
from ..serializers.servicioSerializer import RecienteSerializer, FavoritoSerializer


class RecientesView(viewsets.ModelViewSet):
    queryset = Recientes.objects.all()
    serializer_class = RecienteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_usuario__id',)


class FavoritosView(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        usuario_id = self.request.query_params.get('id_usuario', None)
        if usuario_id is not None:
            return Favoritos.objects.filter(id_usuario__id=usuario_id)
        else:
            return Favoritos.objects.none()  # Retorna un queryset vacío si no hay usuario_id

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Expandir la información de archivos en el resultado
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = FavoritoSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = FavoritoSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

