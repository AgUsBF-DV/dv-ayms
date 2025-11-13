from decimal import Decimal
from django.test import TestCase
from django.utils import timezone

from ventas.models import Venta, VentaLibro
from clientes.models import Cliente
from libros.models import Libro
from autores.models import Autor
from categorias.models import Categoria
from editoriales.models import Editorial
from empleados.models import Empleado


class VentaModelTest(TestCase):
    """Test suite para el modelo Venta"""

    def setUp(self):
        """Configuración inicial para las pruebas"""
        # Crear usuario empleado
        self.empleado = Empleado.objects.create_user(
            username='empleado1',
            email='empleado@test.com',
            password='testpass123'
        )

        # Crear cliente
        self.cliente = Cliente.objects.create(
            nombre='Juan',
            apellido='Pérez',
            correo='juan@test.com'
        )

    def test_venta_creation(self):
        """Test de creación básica de Venta"""
        venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado,
            total=Decimal('1500.00')
        )

        self.assertIsInstance(venta, Venta)
        self.assertEqual(venta.cliente, self.cliente)
        self.assertEqual(venta.empleado, self.empleado)
        self.assertEqual(venta.total, Decimal('1500.00'))
        self.assertIsNotNone(venta.fecha)
        self.assertIsNotNone(venta.created_at)
        self.assertIsNotNone(venta.updated_at)

    def test_venta_str_representation(self):
        """Test del método __str__ de Venta"""
        venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado,
            total=Decimal('2500.00')
        )

        expected_str = f"Venta {venta.id} - Cliente: {self.cliente} - Total: 2500.00 - {venta.fecha:%Y-%m-%d %H:%M}"
        self.assertEqual(str(venta), expected_str)

    def test_venta_default_values(self):
        """Test de valores por defecto en Venta"""
        venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado
        )

        self.assertEqual(venta.total, Decimal('0'))
        # La fecha debe estar cerca del momento actual
        self.assertTrue(
            abs((timezone.now() - venta.fecha).total_seconds()) < 5
        )

    def test_venta_detalle_property(self):
        """Test de la propiedad detalle que devuelve VentaLibro relacionados"""
        venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado
        )

        # Sin libros asociados
        detalle = venta.detalle
        self.assertEqual(len(detalle), 0)


class VentaLibroModelTest(TestCase):
    """Test suite para el modelo VentaLibro"""

    def setUp(self):
        """Configuración inicial para las pruebas"""
        # Crear usuario empleado
        self.empleado = Empleado.objects.create_user(
            username='empleado1',
            email='empleado@test.com',
            password='testpass123'
        )

        # Crear cliente
        self.cliente = Cliente.objects.create(
            nombre='María',
            apellido='González',
            correo='maria@test.com'
        )

        # Crear autor
        self.autor = Autor.objects.create(
            nombre='Gabriel',
            apellido='García Márquez'
        )

        # Crear categoría
        self.categoria = Categoria.objects.create(
            nombre='Literatura'
        )

        # Crear editorial
        self.editorial = Editorial.objects.create(
            nombre='Editorial Planeta'
        )

        # Crear libro
        self.libro = Libro.objects.create(
            titulo='Cien años de soledad',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            precio=Decimal('25000.00'),
            stock=10
        )

        # Crear venta
        self.venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado,
            total=Decimal('0.00')
        )

    def test_venta_libro_creation(self):
        """Test de creación básica de VentaLibro"""
        venta_libro = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=2,
            precio_unitario=Decimal('25000.00'),
            subtotal=Decimal('50000.00')
        )

        self.assertIsInstance(venta_libro, VentaLibro)
        self.assertEqual(venta_libro.venta, self.venta)
        self.assertEqual(venta_libro.libro, self.libro)
        self.assertEqual(venta_libro.cantidad, 2)
        self.assertEqual(venta_libro.precio_unitario, Decimal('25000.00'))
        self.assertEqual(venta_libro.subtotal, Decimal('50000.00'))

    def test_calcular_subtotal_method(self):
        """Test del método calcular_subtotal"""
        venta_libro = VentaLibro(
            venta=self.venta,
            libro=self.libro,
            cantidad=3,
            precio_unitario=Decimal('25000.00')
        )

        # Antes de calcular (puede ser None o 0)
        self.assertIn(venta_libro.subtotal, [None, 0])

        # Calcular subtotal
        venta_libro.calcular_subtotal()

        # Verificar resultado
        expected_subtotal = Decimal('25000.00') * 3
        self.assertEqual(venta_libro.subtotal, expected_subtotal)

    def test_subtotal_calculation_on_save(self):
        """Test que el subtotal se calcula automáticamente al guardar"""
        venta_libro = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=4,
            precio_unitario=Decimal('25000.00')
        )

        # El subtotal debe calcularse automáticamente
        expected_subtotal = Decimal('25000.00') * 4
        self.assertEqual(venta_libro.subtotal, expected_subtotal)

    def test_precio_unitario_default_from_libro(self):
        """Test que el precio_unitario toma el valor del libro si no se especifica"""
        venta_libro = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=1
            # No especificamos precio_unitario
        )

        # Debe tomar el precio del libro
        self.assertEqual(venta_libro.precio_unitario, self.libro.precio)
        self.assertEqual(venta_libro.subtotal, self.libro.precio)

    def test_subtotal_equals_cantidad_times_precio(self):
        """Test que subtotal == cantidad * precio_unitario"""
        test_cases = [
            (1, Decimal('25000.00')),
            (2, Decimal('30000.00')),
            (5, Decimal('15000.00')),
            (10, Decimal('12500.00')),
        ]

        for cantidad, precio in test_cases:
            with self.subTest(cantidad=cantidad, precio=precio):
                venta_libro = VentaLibro.objects.create(
                    venta=self.venta,
                    libro=self.libro,
                    cantidad=cantidad,
                    precio_unitario=precio
                )

                expected_subtotal = cantidad * precio
                self.assertEqual(venta_libro.subtotal, expected_subtotal)

    def test_venta_libro_with_zero_values(self):
        """Test con valores cero o None"""
        venta_libro = VentaLibro(
            venta=self.venta,
            libro=self.libro,
            cantidad=None,
            precio_unitario=None
        )

        venta_libro.calcular_subtotal()

        # Debe manejar valores None como 0
        self.assertEqual(venta_libro.subtotal, 0)

    def test_venta_libro_ordering(self):
        """Test del ordenamiento de VentaLibro (por -id)"""
        venta_libro_1 = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=1,
            precio_unitario=Decimal('25000.00')
        )

        venta_libro_2 = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=2,
            precio_unitario=Decimal('25000.00')
        )

        # Debe ordenarse por -id (más reciente primero)
        venta_libros = list(VentaLibro.objects.all())
        self.assertEqual(venta_libros[0], venta_libro_2)
        self.assertEqual(venta_libros[1], venta_libro_1)


class VentaIntegrationTest(TestCase):
    """Tests de integración entre Venta y VentaLibro"""

    def setUp(self):
        """Configuración inicial para las pruebas de integración"""
        # Crear usuario empleado
        self.empleado = Empleado.objects.create_user(
            username='empleado1',
            email='empleado@test.com',
            password='testpass123'
        )

        # Crear cliente
        self.cliente = Cliente.objects.create(
            nombre='Ana',
            apellido='Martín',
            correo='ana@test.com'
        )

        # Crear autor
        self.autor = Autor.objects.create(
            nombre='Isabel',
            apellido='Allende'
        )

        # Crear categoría
        self.categoria = Categoria.objects.create(
            nombre='Ficción'
        )

        # Crear editorial
        self.editorial = Editorial.objects.create(
            nombre='Editorial Sudamericana'
        )

        # Crear múltiples libros
        self.libro1 = Libro.objects.create(
            titulo='La casa de los espíritus',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            precio=Decimal('28000.00'),
            stock=15
        )

        self.libro2 = Libro.objects.create(
            titulo='Eva Luna',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            precio=Decimal('32000.00'),
            stock=8
        )

    def test_venta_with_multiple_libros(self):
        """Test de venta con múltiples libros"""
        venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado
        )

        # Agregar primer libro
        venta_libro_1 = VentaLibro.objects.create(
            venta=venta,
            libro=self.libro1,
            cantidad=2,
            precio_unitario=self.libro1.precio
        )

        # Agregar segundo libro
        venta_libro_2 = VentaLibro.objects.create(
            venta=venta,
            libro=self.libro2,
            cantidad=1,
            precio_unitario=self.libro2.precio
        )

        # Verificar que ambos libros están asociados
        libros_en_venta = venta.libros.all()
        self.assertEqual(len(libros_en_venta), 2)
        self.assertIn(venta_libro_1, libros_en_venta)
        self.assertIn(venta_libro_2, libros_en_venta)

        # Verificar subtotales
        expected_subtotal_1 = Decimal('28000.00') * 2
        expected_subtotal_2 = Decimal('32000.00') * 1

        self.assertEqual(venta_libro_1.subtotal, expected_subtotal_1)
        self.assertEqual(venta_libro_2.subtotal, expected_subtotal_2)

    def test_venta_detalle_property_with_libros(self):
        """Test de la propiedad detalle con libros asociados"""
        venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado
        )

        VentaLibro.objects.create(
            venta=venta,
            libro=self.libro1,
            cantidad=1,
            precio_unitario=self.libro1.precio
        )

        VentaLibro.objects.create(
            venta=venta,
            libro=self.libro2,
            cantidad=3,
            precio_unitario=self.libro2.precio
        )

        detalle = venta.detalle
        self.assertEqual(len(detalle), 2)


class VentaLibroEdgeCasesTest(TestCase):
    """Tests para casos extremos y edge cases"""

    def setUp(self):
        """Configuración básica"""
        self.empleado = Empleado.objects.create_user(
            username='empleado1',
            email='empleado@test.com',
            password='testpass123'
        )

        self.cliente = Cliente.objects.create(
            nombre='Test',
            apellido='User',
            correo='test@test.com'
        )

        self.autor = Autor.objects.create(
            nombre='Autor',
            apellido='Test'
        )

        self.categoria = Categoria.objects.create(nombre='Test')
        self.editorial = Editorial.objects.create(nombre='Test Editorial')

        self.libro = Libro.objects.create(
            titulo='Libro Test',
            autor=self.autor,
            editorial=self.editorial,
            categoria=self.categoria,
            precio=Decimal('10000.00'),
            stock=5
        )

        self.venta = Venta.objects.create(
            cliente=self.cliente,
            empleado=self.empleado
        )

    def test_subtotal_with_decimal_precision(self):
        """Test de precisión decimal en cálculo de subtotal"""
        venta_libro = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=3,
            precio_unitario=Decimal('33.33')
        )

        # 3 * 33.33 = 99.99
        expected_subtotal = Decimal('99.99')
        self.assertEqual(venta_libro.subtotal, expected_subtotal)

    def test_large_quantities_and_prices(self):
        """Test con cantidades y precios grandes"""
        venta_libro = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=1000,
            precio_unitario=Decimal('999999.99')
        )

        expected_subtotal = Decimal('1000') * Decimal('999999.99')
        self.assertEqual(venta_libro.subtotal, expected_subtotal)

    def test_minimum_values(self):
        """Test con valores mínimos"""
        venta_libro = VentaLibro.objects.create(
            venta=self.venta,
            libro=self.libro,
            cantidad=1,
            precio_unitario=Decimal('0.01')
        )

        expected_subtotal = Decimal('0.01')
        self.assertEqual(venta_libro.subtotal, expected_subtotal)
