import unittest
from automation import Automation

automation = Automation()
class Automation(unittest.TestCase):


    def test_buscar(self):
        titulo = "dodge 2000 stratus balatas"
        texto_resultado = automation.buscar(titulo)
        self.assertEqual(texto_resultado, "Hay 13 productos.")
        automation.cerrar()


if __name__ == "__main__":
    unittest.main()