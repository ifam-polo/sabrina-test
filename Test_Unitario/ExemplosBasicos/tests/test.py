
from unittest import TestCase
from apps.aplicacao1 import conversao_para_celsius, conversão_para_fahrenheit


class TestConverteFparaC(TestCase):
    def test_converte_deve_retornar_0_quando_receber_32(self):
        assert conversao_para_celsius(32) == 0
        
    def test_convete_deve__40_quando__40(self):
        self.assertEqual(conversao_para_celsius(-40), -40)
        
    def test_convert_deve_retornar_17_77_receber_0(self):
        self.assertAlmostEqual(conversao_para_celsius(0), -17.77, places=1)
              
class  TestConverteCparaF(TestCase):
    def test_converte_deve_retorna_40_quando_receber_40(self):
        assert conversão_para_fahrenheit(-40) == -40