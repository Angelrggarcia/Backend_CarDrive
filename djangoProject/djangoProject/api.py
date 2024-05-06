from rest_framework.response import Response
from rest_framework.veiws import APIView
from proyectos.models import proyectos
from proyectos.serializers import ProyectosSerializer
from unidades.models import unidades
from unidades.serializers import UnidadesSerializer

class proyectosAPIViews(APIView):
    def get(self, request):
        proyectos = proyectos.objects.all()
        proyectos_serializer = ProyectosSerializer(proyectos, many = True)
        return Response(proyectos_serializer.data)
    
    def post(self, request):
        serializer = ProyectosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class unidadesAPIViews(APIView):
    def get(self, request):
        unidades = unidades.objects.all()
        unidades_serializer = UnidadesSerializer(unidades, many = True)
        return Response(unidades_serializer.data)
    
    def post(self, request):
        serializer = UnidadesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)