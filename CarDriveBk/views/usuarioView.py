from rest_framework import viewsets

from ..models.users import Usuarios
from ..serializers.usuarioSerializer import UsuarioSerializer


class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

