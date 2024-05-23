from rest_framework import viewsets

from ..models.versiones import Versiones
from ..serializers.versionSerializer import VersionSerializer


class VersionsView(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionSerializer
    
    # @action(detail=True, methods=['get'])
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

