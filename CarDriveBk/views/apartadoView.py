from rest_framework import viewsets, filters

from ..models.apartado import Apartados
from ..serializers.apartadosSerializer import ApartadosSerializer


class ApartadoView(viewsets.ModelViewSet):
    serializer_class = ApartadosSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_proyecto__id',)

    def get_queryset(self):
        """
        Opcionalmente filtra por tipo de apartado: Unidad o Carpeta.
        """
        queryset = Apartados.objects.all()
        tipo = self.request.query_params.get('tipo', None)
        id_proyecto = self.request.query_params.get('id_proyecto', None)

        if tipo == "unidad":
            queryset = queryset.filter(id_padre__isnull=True)
        elif tipo == "carpeta":
            queryset = queryset.exclude(id_padre__isnull=True)

        if id_proyecto:
            queryset = queryset.filter(id_proyecto__id=id_proyecto)

        return queryset
