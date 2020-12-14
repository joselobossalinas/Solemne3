from django.test import TestCase
from .models import Contacto

# Create your tests here.

class ContactoTestCase(TestCase):
    def setUp(self):
        self.Contacto1 = Contacto.objects.create(
            nombre="Enrique",
            correo="erojas@duoc.cl",
            numero="951796542",
            )
        self.Contacto2 = Contacto.objects.create(
            nombre="José",
            correo="jlobos@duoc.cl",
            numero="951796544",)

    def test_Contacto_nombre1(self):
        self.assertEqual(self.Contacto1.nombre, 'Enrique')

    def test_Contacto_nombre2(self):
        self.assertEqual(self.Contacto2.nombre, 'José')
    
    def test_Contacto_correo1(self):
        self.assertEqual(self.Contacto1.correo, 'erojas@duoc.cl')
    
    def test_Contacto_correo2(self):
        self.assertEqual(self.Contacto2.correo, 'jlobos@duoc.cl')

    def test_Contacto_numero1(self):
        self.assertEqual(self.Contacto1.numero, '951796542')

    def test_Contacto_numero2(self):
        self.assertEqual(self.Contacto2.numero, '951796544')    

   