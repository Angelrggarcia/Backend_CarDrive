from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models.versiones import Versiones


class VersionSerializer(serializers.ModelSerializer):
    documents = Base64ImageField(required=False)
    class Meta:
        model = Versiones
        fields = '__all__'