from rest_framework import generics, viewsets

from ..models.archivos import Archivos
from ..serializers.archivosSerializer import ArchivoSerializer



class ArchivosView(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    serializer_class = ArchivoSerializer


class ArchivosListCreate(generics.ListCreateAPIView):
    queryset = Archivos
    serializer_class = ArchivoSerializer


class ArchivosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archivos
    serializer_class = ArchivoSerializer

