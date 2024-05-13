from rest_framework import generics

from ..models.versiones import Version
from ..serializers.versionSerializer import VersionSerializer


class VersionListCreate(generics.ListCreateAPIView):
    queryset = Version
    serializer_class = VersionSerializer


class VersionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Version
    serializer_class = VersionSerializer
