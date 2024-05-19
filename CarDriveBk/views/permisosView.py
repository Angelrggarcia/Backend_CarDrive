from rest_framework import viewsets

from ..models.permisos import Proyectleader, Coordinador, Miembros
from ..serializers.permisosSerializer import ProyectoLeaderSerializer, CoordinadorSerializer, MiembroSerializer


class ProyectoleaderView(viewsets.ModelViewSet):
    queryset = Proyectleader.objects.all()
    serializer_class = ProyectoLeaderSerializer


class CoordinadoresView(viewsets.ModelViewSet):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer


class MiembrosView(viewsets.ModelViewSet):
    queryset = Miembros.objects.all()
    serializer_class = MiembroSerializer
