import unittest

class TestStart(unittest.TestCase):

    def setUp(self):
        # Configuración antes de cada prueba
        pass

    def tearDown(self):
        # Limpieza después de cada prueba
        pass

    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
