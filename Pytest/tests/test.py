from codigo.app import bricadeira 

def test_quando_bricadeira_recerber_1_entao_retorna_1():
    assert bricadeira(1) == 1
    
def test_quando_bricadeira_recerber_qualquer_numero_entao_retorna_1():
    assert bricadeira(4) == 2