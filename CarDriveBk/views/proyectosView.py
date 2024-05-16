from rest_framework import viewsets

from ..models.proyectos import Proyectos
from ..serializers.proyectoSerializer import ProyectoSerializer


class ProyectosView(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectoSerializer

