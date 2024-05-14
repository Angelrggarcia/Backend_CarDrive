from rest_framework import generics, viewsets

from ..models.permisos import Proyectleader, Coordinador, Miembro
from ..serializers.permisosSerializer import ProyectoLeaderSerializer, CoordinadorSerializer, MiembroSerializer


class ProyectoleaderView(viewsets.ModelViewSet):
    queryset = Proyectleader.objects.all()
    serializer_class = ProyectoLeaderSerializer


class ProyectleaderListCreate(generics.ListCreateAPIView):
    queryset = Proyectleader.objects.all()
    serializer_class = ProyectoLeaderSerializer


class ProyectleaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyectleader.objects.all()
    serializer_class = ProyectoLeaderSerializer


class CoordinadorListCreate(generics.ListCreateAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer


class CoordinadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer


class MiembroListCreate(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer


class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
