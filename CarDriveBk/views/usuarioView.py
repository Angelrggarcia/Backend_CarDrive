from rest_framework import viewsets

from ..models.users import Usuario
from ..serializers.usuarioSerializer import UsuarioSerializer


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

