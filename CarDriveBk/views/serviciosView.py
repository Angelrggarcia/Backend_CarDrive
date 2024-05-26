from rest_framework import viewsets, filters

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
    search_fields = ('id_usuario__id',)

