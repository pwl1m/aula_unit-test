import unittest #estrutura
from calculadora import soma #importando do calculadora.py a função soma

class TestCalculadora(unittest.TestCase): #estrutura
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5), 10)
        
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5), 0)
        
    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (-10, 10, 0),
            (5.5, 5.5, 11),
            ('10', 5, 15)
        )
        for x_y_saida in x_y_saidas:
            # with - gerenciador de contexto (pesquisar)
            with self.subTest(x_y_saida=x_y_saida):
                x,y, saida = x_y_saida
                self.assertEqual(soma(x,y), saida)
                
    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertion_error(self):
        #assertRaises serve para testar se o erro está sendo retornado 
        #assertionError é o erro que deve ser retornado quando a entrada não é int ou float
        with self.assertRaises(AssertionError):
            soma('10', 5)
            
unittest.main(verbosity=True) #estrutura de teste unitario - rodar no terminal python -m unittest test_calculadora.py