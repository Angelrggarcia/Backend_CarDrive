from rest_framework import generics, viewsets

from ..models.versiones import Versiones
from ..serializers.versionSerializer import VersionSerializer


class VersionsView(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionSerializer

