from rest_framework import serializers

from ..models.versiones import Versiones


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versiones
        fields = '__all__'
