from app.main import Coluna

def test_coluna_deve_ter_um_nome():
    assert Coluna('Fazendo').nome == 'Fazendo'