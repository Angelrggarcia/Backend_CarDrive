from rest_framework import viewsets

from ..models.etiquetas import Etiquetas, RelacionesEtiquetas
from ..serializers.etiquetasSerializer import EtiquetaSerializer, RelacionesEtiquetaSerializer


class EtiquetasView(viewsets.ModelViewSet):
    queryset = Etiquetas.objects.all()
    serializer_class = EtiquetaSerializer


class RelacionesEtiquetasView(viewsets.ModelViewSet):
    queryset = RelacionesEtiquetas.objects.all()
    serializer_class = RelacionesEtiquetaSerializer
