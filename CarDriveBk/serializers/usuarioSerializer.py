from rest_framework import serializers

from ..models.users import Usuarios


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'