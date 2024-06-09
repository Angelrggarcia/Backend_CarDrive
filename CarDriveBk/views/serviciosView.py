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
        # Filtra los favoritos para el usuario autenticado
        user = self.request.user
        if user.is_authenticated:
            return Favoritos.objects.filter(id_usuario=user)
        else:
            return Favoritos.objects.none()

