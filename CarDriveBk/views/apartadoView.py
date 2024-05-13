from rest_framework import generics, viewsets

from ..models.apartado import Apartado
from ..serializers.apartadosSerializer import ApartadosSerializer

class ApartadoView(viewsets.ModelViewSet):
    queryset = Apartado.objects.all()
    serializer_class = ApartadosSerializer

class ApartadoListCreate(generics.ListCreateAPIView):
    queryset = Apartado
    serializer_class = ApartadosSerializer


class ApartadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartado
    serializer_class = ApartadosSerializer
