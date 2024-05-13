from rest_framework import generics, viewsets

from ..models.proyectos import Proyecto, Archivados
from ..serializers.proyectoSerializer import ProyectoSerializer, ArchivadosSerializer


class ProyectoListCreate(generics.ListCreateAPIView):
    queryset = Proyecto
    serializer_class = ProyectoSerializer


class ProyectoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto
    serializer_class = ProyectoSerializer


class ProyectoView(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ArchivadosView(viewsets.ModelViewSet):
    queryset = Archivados.objects.all()
    serializer_class = ArchivadosSerializer

class ArchivadosListCreate(generics.ListCreateAPIView):
    queryset = Archivados
    serializer_class = ArchivadosSerializer


class ArchivadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archivados
    serializer_class = ArchivadosSerializer
