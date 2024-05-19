from rest_framework import viewsets, filters

from ..models.apartado import Apartados
from ..serializers.apartadosSerializer import ApartadosSerializer
from rest_framework.response import Response

class ApartadoView(viewsets.ModelViewSet):
    queryset = Apartados.objects.all()  # Add this line
    serializer_class = ApartadosSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nombre', 'id')
