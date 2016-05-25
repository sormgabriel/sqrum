import unittest

class ClaseDePrueba:
    def saluda(self):
        return "hola SQRUM"

class ClaseDePruebaTest(unittest.TestCase):
    
    def test_saluda(self):
        #arrange
            self.obj = ClaseDePrueba()
        #act
            self.res = self.obj.saluda()
        #assert
            self.assertEqual(self.res, "hola SQRUM")