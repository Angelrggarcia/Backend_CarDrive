# views.py
from rest_framework import viewsets
from ..models.apartado import Apartados
from ..serializers.apartadosSerializer import ApartadosSerializer
from rest_framework.response import Response

class ApartadoView(viewsets.ModelViewSet):
    queryset = Apartados.objects.all()  # Add this line
    serializer_class = ApartadosSerializer

    def get_queryset(self):
        queryset = Apartados.objects.all()
        proyecto_id = self.request.query_params.get('proyectoId', None)
        if proyecto_id is not None:
            queryset = queryset.filter(proyecto_id=proyecto_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
