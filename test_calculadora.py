import unittest #estrutura
from calculadora import soma #importando do calculadora.py a função soma

class TestCalculadora(unittest.TestCase): #estrutura
    def test_soma_5e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)

unittest.main(verbosity=True) #estrutura de teste unitario - rodar no terminal python -m unittest test_calculadora.py