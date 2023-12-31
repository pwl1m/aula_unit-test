"""
TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Red
Pt1 - Criar o teste e ver falhar

Green
Pt2 - Criar o código e ver o teste passar

Refactor 
Pt3 - Refatorar o código (Melhorar) 
"""

import unittest
from baconcomovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_sen_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')
            
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                            msg=f'"{entrada}" Saida: "{saida}"')
            
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nfor_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar Fome'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                        msg=f'"{entrada}" Saida: {saida}"')

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3,6,9,12,18,21)
        saida = 'Bacon'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                        msg=f'"{entrada}" Saida: "{saida}"')

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_5(self):
        entradas = (5,10,20,25,35,40)
        saida = 'Ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                        msg=f'"{entrada}" Saida: "{saida}"')

unittest.main(verbosity=2)