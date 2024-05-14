from rest_framework import viewsets

from ..models.etiquetas import Etiquetas, Asociar_etiquetas
from ..serializers.etiquetasSerializer import EtiquetaSerializer, AsociacionEtiquetaSerializer


class EtiquetasView(viewsets.ModelViewSet):
    queryset = Etiquetas.objects.all()
    serializer_class = EtiquetaSerializer

class Asociar_etiquetasView(viewsets.ModelViewSet):
    queryset = Asociar_etiquetas.objects.all()
    serializer_class = AsociacionEtiquetaSerializer

