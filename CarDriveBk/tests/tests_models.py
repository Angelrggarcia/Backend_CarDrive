# myapp/tests/test_models.py
from django.test import TestCase
from django.utils import timezone
from ..models.apartado import Apartados
from ..models.archivos import Archivos
from ..models.etiquetas import Etiquetas, RelacionesEtiquetas
from ..models.permisos import Proyectleader, Coordinador, Miembros
from ..models.proyectos import Proyectos
from ..models.servicios import Favoritos, Recientes
from ..models.users import Usuarios
from ..models.versiones import Versiones

class ModelTests(TestCase):

    def setUp(self):
        self.user = Usuarios.objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
            color="FFFFFF",
            fecha=timezone.now()
        )

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

        self.relacion_etiqueta = RelacionesEtiquetas.objects.create(
            id_archivos=self.archivo,
            id_etiquetas=self.etiqueta
        )

        self.favorito = Favoritos.objects.create(
            id_usuario=self.user,
            id_archivo=self.archivo
        )

        self.reciente = Recientes.objects.create(
            id_usuario=self.user,
            id_archivo=self.archivo
        )

        self.version = Versiones.objects.create(
            id_archivo=self.archivo,
            iteracion=1,
            archivo=None
        )

        self.proyectleader = Proyectleader.objects.create(
            id_proyecto=self.proyecto,
            id_usuario=self.user
        )

        self.coordinador = Coordinador.objects.create(
            id_apartado=self.apartado,
            id_usuario=self.user
        )

        self.miembro = Miembros.objects.create(
            id_apartado=self.apartado,
            id_usuario=self.user
        )

    def test_apartado_str(self):
        self.assertEqual(str(self.apartado), f"{self.apartado.id} - {self.apartado.nombre}")

    def test_archivo_str(self):
        self.assertEqual(str(self.archivo), self.archivo.nombre)

    def test_etiqueta_str(self):
        self.assertEqual(str(self.etiqueta), self.etiqueta.nombre)

    def test_relacion_etiqueta_str(self):
        self.assertEqual(str(self.relacion_etiqueta), f" {self.archivo} {self.etiqueta}")

    def test_proyecto_str(self):
        self.assertEqual(str(self.proyecto), self.proyecto.nombre)

    def test_favorito_str(self):
        self.assertEqual(str(self.favorito), f"{self.user} - {self.archivo}")

    def test_reciente_str(self):
        self.assertEqual(str(self.reciente), f"{self.user} - {self.archivo}")

    def test_usuario_str(self):
        self.assertEqual(str(self.user), self.user.first_name)

    def test_version_str(self):
        self.assertEqual(str(self.version), f"{self.archivo} - {self.version.iteracion}")

    def test_proyectleader_str(self):
        self.assertEqual(str(self.proyectleader), str(self.user))

    def test_coordinador_str(self):
        self.assertEqual(str(self.coordinador), str(self.user))

    def test_miembro_str(self):
        self.assertEqual(str(self.miembro), str(self.user))
