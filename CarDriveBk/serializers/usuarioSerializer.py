from rest_framework import serializers
from datetime import datetime
from ..models.users import Usuarios

class CustomDateField(serializers.DateField):
    def to_representation(self, value):
        # Representing date in DD/MM/YYYY format
        return value.strftime('%d/%m/%Y')

    def to_internal_value(self, data):
        try:
            # Parsear la fecha en formato YYYY-MM-DD
            return datetime.strptime(data, '%Y-%m-%d').date()
        except ValueError:
            self.fail('invalid', format='YYYY-MM-DD')

class UsuarioSerializer(serializers.ModelSerializer):
    fecha = CustomDateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'])
    class Meta:
        model = Usuarios
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    # def create(self, validated_data):
    #     user = Usuarios.objects.create_user(**validated_data)
    #     return user
        
class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )
    email = serializers.EmailField(
        required=True
    )