from rest_framework import generics, viewsets

from ..models.versiones import Version
from ..serializers.versionSerializer import VersionSerializer


class VersionsView(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionListCreate(generics.ListCreateAPIView):
    queryset = Version
    serializer_class = VersionSerializer


class VersionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Version
    serializer_class = VersionSerializer
