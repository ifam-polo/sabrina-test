from codigo.app import bricadeira 

def test_quando_bricadeira_recerber_1_entao_retorna_1():
    assert bricadeira(1) == 1
    
def test_quando_bricadeira_recerber_qualquer_numero_entao_retorna_1():
    assert bricadeira(4) == 2
    
    print("Estoy aqui :)")
    
def test_quando_bricadeira_receber_5_retorna_goiabada():
    
    assert bricadeira(5) == 'goiabada'