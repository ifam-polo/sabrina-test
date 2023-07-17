from unittest import TestCase
from aplicacao1 import conversao


class TestConverte(TestCase):
    def test_converte_deve_retornar_0_quando_receber_32(self):
        assert conversao(32) == 0
