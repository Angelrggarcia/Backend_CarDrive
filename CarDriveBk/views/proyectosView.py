from rest_framework import generics, viewsets

from ..models.proyectos import Proyecto, Archivados
from ..serializers.proyectoSerializer import ProyectoSerializer, ArchivadosSerializer


class ProyectoView(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class ArchivadosView(viewsets.ModelViewSet):
    queryset = Archivados.objects.all()
    serializer_class = ArchivadosSerializer
