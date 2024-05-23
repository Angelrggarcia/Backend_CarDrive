from rest_framework import serializers
from datetime import datetime
from ..models.users import Usuarios

class CustomDateField(serializers.DateField):
    def to_representation(self, value):
        # Representing date in DD/MM/YYYY format
        return value.strftime('%d/%m/%Y')

    def to_internal_value(self, data):
        try:
            # Parsing date in YYYY-MM-DD format
            return datetime.strptime(data, '%d/%m/%Y').date()
        except ValueError:
            self.fail('invalid', format='DD/MM/YYYY')

class UsuarioSerializer(serializers.ModelSerializer):
    fecha = datetime.now().strftime('%d/%m/%Y')
    class Meta:
        model = Usuarios
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def create(self, validated_data):
        user = Usuarios.objects.create_user(**validated_data)
        return user
        
class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )
    email = serializers.EmailField(
        required=True
    )