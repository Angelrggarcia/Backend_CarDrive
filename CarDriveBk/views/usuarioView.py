from rest_framework import viewsets

from ..models.users import Usuarios
from ..serializers.usuarioSerializer import UsuarioSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from ..serializers.usuarioSerializer import LoginSerializer



class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
    
    @action(methods=["POST"], detail=False, serializer_class=LoginSerializer, permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def create(self, request):
        serializer = UsuarioSerializer(data=request.data)
        user = None
        if serializer.is_valid():
            user = Usuarios.objects.create_user(
                email = serializer.validated_data["email"], 
                password = serializer.validated_data["password"], 
                first_name = serializer.validated_data["first_name"], 
                last_name = serializer.validated_data["last_name"], 
                #last_login = serializer.validated_data["last_login"],
            )
            user.last_login = timezone.now()  # Instead of validating data, set the last login manually to right now since it wont get posted
            user.save()
            response = UsuarioSerializer(instance=user, context={'request': request} )

            return Response(response.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


