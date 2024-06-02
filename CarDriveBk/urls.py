"""
URL configuration for CarDriveBk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
from rest_framework_simplejwt import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# Rutas para las vistas
router = DefaultRouter()
router.register("proyectos", ProyectosView)
router.register("usuarios", UsuariosView)
router.register("apartados", ApartadoView)
router.register("lideres", ProyectoleaderView)
router.register("coordinadores", CoordinadoresView)
router.register("miembros", MiembrosView)
router.register(r'archivos', ArchivosView)
router.register("etiquetas", EtiquetasView)
router.register("retiquetas", RelacionesEtiquetasView)
router.register(r'versiones', VersionsView)
router.register("favoritos", FavoritosView)
router.register("recientes", RecientesView)

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
