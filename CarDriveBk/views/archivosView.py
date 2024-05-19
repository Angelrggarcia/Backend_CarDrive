from rest_framework import viewsets

from ..models.archivos import Archivos
from ..serializers.archivosSerializer import ArchivoSerializer


class ArchivosView(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    serializer_class = ArchivoSerializer
