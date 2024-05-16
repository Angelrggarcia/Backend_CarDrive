from rest_framework import generics, viewsets

from ..models.servicios import Recientes, Favoritos
from ..serializers.servicioSerializer import RecienteSerializer, FavoritoSerializer


class RecientesView(viewsets.ModelViewSet):
    queryset = Recientes.objects.all()
    serializer_class = RecienteSerializer


class FavoritosView(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer

