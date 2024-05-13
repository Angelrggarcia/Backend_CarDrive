from rest_framework import viewsets
from ..models.proyectos import Proyecto
from ..serializers.proyectoSerializer import ProyectoSerializer

class ProyectoView(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer