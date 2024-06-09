from django.db.models import Q
from rest_framework import viewsets, filters

from ..models.apartado import Apartados
from ..serializers.apartadosSerializer import ApartadoSerializer


class ApartadoView(viewsets.ModelViewSet):
    serializer_class = ApartadoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_proyecto__id', 'id_padre__id',)

    def get_queryset(self):
        queryset = Apartados.objects.all()
        id_proyecto = self.request.query_params.get('id_proyecto__id')
        id_padre = self.request.query_params.get('id_padre__id')

        if id_padre:
            queryset = queryset.filter(id_padre__id=id_padre)
        elif id_proyecto:
            queryset = queryset.filter(Q(id_proyecto__id=id_proyecto) & Q(id_padre__isnull=True))

        print(f"Filtrando por id_proyecto: {id_proyecto}, id_padre: {id_padre}")
        print(f"Queryset resultante: {queryset.query}")
        return queryset