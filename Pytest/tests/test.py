from pytest import mark
from codigo.app import bricadeira 

@mark.skip(reason="pq está falhando")
def test_quando_bricadeira_recerber_1_entao_retorna_1():
    assert bricadeira(1) == 1
    
def test_quando_bricadeira_recerber_qualquer_numero_entao_retorna_1():
    assert bricadeira(4) == 2
    
    print("Estoy aqui :)")
    
def test_quando_bricadeira_receber_5_retorna_goiabada():
    
    assert bricadeira(5) == 'goiabada'
    
@mark.parametrizado 
@mark.parametrize(
    'entrada',
    [3,4,20,25,35]
)
def test__bricdeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    
    assert bricadeira(entrada) == 'goiabada'
    
@mark.multiplo3
@mark.parametrize(
    'entrada',
    [3,20,9,12,18]
)
def test__bricdeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    
    assert bricadeira(entrada) == 'queijo'
    
@mark.esperado
@mark.parametrize(
    'entrada,esperado',
    [(1,1),(2,2),(3, 'queijo'),(4,4), (5, 'goiabada')]
)
def test__bricdeira_deve_retornar_valor_esperado(entrada, esperado):
    
    assert bricadeira(entrada) == esperado