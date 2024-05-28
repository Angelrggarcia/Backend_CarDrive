# myapp/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models.apartado import Apartados
from ..models.archivos import Archivos
from ..models.etiquetas import Etiquetas, RelacionesEtiquetas
from ..models.permisos import Proyectleader, Coordinador, Miembros
from ..models.proyectos import Proyectos
from ..models.servicios import Favoritos, Recientes
from ..models.users import Usuarios
from ..models.versiones import Versiones
from django.utils import timezone

class ViewTests(TestCase):
    
    
    @pytest.mark.django_db
    def setUp(self):
        self.client = APIClient()
        self.user = Usuarios.objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
            color="FFFFFF",
            fecha=timezone.now()
        )
        
        self.client.force_authenticate(user=self.user)

        self.proyecto = Proyectos.objects.create(
            nombre="Proyecto Test",
            descripcion="Descripción del proyecto",
            color="#FFFFFF",
            imagen=None,
            activo=True,
            creator=self.user
        )

        self.apartado = Apartados.objects.create(
            nombre="Apartado Test",
            color="#FFFFFF",
            fecha=timezone.now(),
            imagen=None,
            id_usuario=self.user,
            id_proyecto=self.proyecto
        )

        self.archivo = Archivos.objects.create(
            nombre="Archivo Test",
            descripcion="Descripción del archivo",
            terminacion=".txt",
            fecha=timezone.now(),
            id_usuarios=self.user,
            id_apartados=self.apartado
        )

        self.etiqueta = Etiquetas.objects.create(
            nombre="Etiqueta Test",
            color="#FFFFFF"
        )

    @pytest.mark.django_db
    def test_apartados_list_view(self):
        response = self.client.get(reverse('apartado-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_archivos_list_view(self):
        response = self.client.get(reverse('archivo-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    @pytest.mark.django_db
    def test_etiquetas_list_view(self):
        response = self.client.get(reverse('etiqueta-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_proyectos_list_view(self):
        response = self.client.get(reverse('proyectos-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_favoritos_list_view(self):
        response = self.client.get(reverse('favorito-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_recientes_list_view(self):
        response = self.client.get(reverse('reciente-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_usuarios_list_view(self):
        response = self.client.get(reverse('usuarios-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_versiones_list_view(self):
        response = self.client.get(reverse('version-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
