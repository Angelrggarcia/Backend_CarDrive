from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
# Imports de vistas
from CarDriveBk.views.registerView import RegisterView
from CarDriveBk.views.usuarioView import UsuariosView
from CarDriveBk.views.proyectosView import ProyectosView
from CarDriveBk.views.apartadoView import ApartadoView
from CarDriveBk.views.archivosView import ArchivosView
from CarDriveBk.views.etiquetasView import EtiquetasView
from CarDriveBk.views.etiquetasView import RelacionesEtiquetasView
from CarDriveBk.views.versionView import VersionsView
from CarDriveBk.views.permisosView import ProyectoleaderView, CoordinadoresView, MiembrosView
from CarDriveBk.views.serviciosView import RecientesView
from CarDriveBk.views.serviciosView import FavoritosView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# Rutas para las vistas
router = DefaultRouter()
router.register("proyectos", ProyectosView, basename='proyecto')
router.register("usuarios", UsuariosView, basename='usuario')
router.register("apartados", ApartadoView, basename='apartado')
router.register("lideres", ProyectoleaderView, basename='lider')
router.register("coordinadores", CoordinadoresView, basename='coordinador')
router.register("miembros", MiembrosView, basename='miembro')
router.register("archivos", ArchivosView, basename='archivo')
router.register("etiquetas", EtiquetasView, basename='etiqueta')
router.register("retiquetas", RelacionesEtiquetasView, basename='retiqueta')
router.register("versiones", VersionsView, basename='version')
router.register("favoritos", FavoritosView, basename='favorito')
router.register("recientes", RecientesView, basename='reciente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
