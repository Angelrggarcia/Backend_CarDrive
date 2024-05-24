from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from django.core.exceptions import ObjectDoesNotExist
from ..models.versiones import Versiones
from ..serializers.versionSerializer import VersionSerializer

class VersionsView(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id_archivo', 'iteracion')

    @action(detail=True, methods=['get'], url_path='download/(?P<iteracion>[^/.]+)')
    def download(self, request, pk=None, iteracion=None):
        try:
            # Buscar el documento
            version = Versiones.objects.get(id_archivo=pk, iteracion=iteracion)
            documento = version.archivo
            documento_path = documento.path
            original_filename = documento.name.split('/')[-1]
            
            # Crear la respuesta de archivo
            response = FileResponse(open(documento_path, 'rb'))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = f'attachment; filename="{original_filename}"'
            return response
        except ObjectDoesNotExist:
            return Response({"detail": "Version not found."}, status=status.HTTP_404_NOT_FOUND)
        except FileNotFoundError:
            return Response({"detail": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Capturar cualquier otra excepción y registrar el error
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error downloading file: {str(e)}")
            return Response({"detail": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
          
    # @action(detail=True, methods=['get'], )
    # def download(self, request, pk=None):
    #     version = self.get_object()
    #     file = version.archivo
    #     return file
    
# def upload_file(request):
#     if request.method == 'POST':
#         form = VersionSerializer(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('File uploaded successfully')
            
#     else:
#         form = VersionSerializer()
#     return render(request, 'upload.html', {'form': form})

