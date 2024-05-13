from rest_framework import generics

from ..models.archivos import Archivos, Etiquetas, Asociar_etiquetas
from ..serializers.archivosSerializer import ArchivoSerializer, EtiquetaSerializer, AsociacionEtiquetaSerializer


class ArchivosListCreate(generics.ListCreateAPIView):
    queryset = Archivos
    serializer_class = ArchivoSerializer


class ArchivosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archivos
    serializer_class = ArchivoSerializer


class EtiquetasListCreate(generics.ListCreateAPIView):
    queryset = Etiquetas
    serializer_class = EtiquetaSerializer


class EtiquetasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etiquetas
    serializer_class = EtiquetaSerializer


class Asociar_etiquetasCreate(generics.ListCreateAPIView):
    queryset = Asociar_etiquetas
    serializer_class = AsociacionEtiquetaSerializer


class Asociar_etiquetasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asociar_etiquetas
    serializer_class = AsociacionEtiquetaSerializer
