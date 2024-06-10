from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models.users import Usuarios
from ..serializers.usuarioSerializer import UsuarioSerializer, LoginSerializer

class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [JWTAuthentication]
    
    def create(self, request):
        
        data = request.data.copy()  # Copia los datos de la solicitud
        data['fecha'] = timezone.now().date().strftime('%Y-%m-%d') 

        serializer = UsuarioSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()
            response = UsuarioSerializer(instance=user, context={'request': request})
            return Response(response.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=["POST"], detail=False, serializer_class=LoginSerializer, permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                user = Usuarios.objects.get(email=email)
            except Usuarios.DoesNotExist:
                raise ValidationError({"error": "User not found"})

            if not user.check_password(password):
                raise ValidationError({"error": "Incorrect Password"})
            
            user.last_login = timezone.now() 
            user.save()

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'refresh': str(refresh),
                'access': access_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    