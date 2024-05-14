from rest_framework import generics, viewsets

from ..models.servicios import Recientes, Favoritos
from ..serializers.servicioSerializer import RecienteSerializer, FavoritoSerializer


class RecientesListCreate(generics.ListCreateAPIView):
    queryset = Recientes
    serializer_class = RecienteSerializer


class RecientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recientes
    serializer_class = RecienteSerializer


class RecientesView(viewsets.ModelViewSet):
    queryset = Recientes.objects.all()
    serializer_class = RecienteSerializer


class FavoritosView(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer


class FavoritosListCreate(generics.ListCreateAPIView):
    queryset = Favoritos
    serializer_class = FavoritoSerializer


class FavoritosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favoritos
    serializer_class = FavoritoSerializer
