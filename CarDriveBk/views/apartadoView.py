from rest_framework import generics, viewsets

from ..models.apartado import Apartados
from ..serializers.apartadosSerializer import ApartadosSerializer


class ApartadoView(viewsets.ModelViewSet):
    queryset = Apartados.objects.all()
    serializer_class = ApartadosSerializer
