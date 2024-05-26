from rest_framework import viewsets, filters

from ..models.permisos import Proyectleader, Coordinador, Miembros
from ..serializers.permisosSerializer import ProyectoLeaderSerializer, CoordinadorSerializer, MiembroSerializer


class ProyectoleaderView(viewsets.ModelViewSet):
    queryset = Proyectleader.objects.all()
    serializer_class = ProyectoLeaderSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_proyecto__id',)


class CoordinadoresView(viewsets.ModelViewSet):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_apartado__id',)


class MiembrosView(viewsets.ModelViewSet):
    queryset = Miembros.objects.all()
    serializer_class = MiembroSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_apartado__id',)
