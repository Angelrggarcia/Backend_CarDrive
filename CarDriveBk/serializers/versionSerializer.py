from drf_extra_fields.fields import Base64FileField
from rest_framework import serializers

from ..models.versiones import Versiones


class VersionSerializer(serializers.ModelSerializer):
    archivo = serializers.FileField(max_length=None, allow_empty_file=False, use_url=False)

    class Meta:
        model = Versiones
        fields = '__all__'
        # widgets = {
        #     'archivo': 
        # }