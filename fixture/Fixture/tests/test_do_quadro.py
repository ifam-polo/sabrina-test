from app.main import Quadro, Coluna, Tarefa
from pytest import fixture

@fixture
def quadro():
   # print("Estou montando o quadro! \n ")
    yield Quadro()
   # print("Estou desmontando o quadro! \n")

def test_nao_deve_existir_nenhuma_cluna_no_quadro(quadro):
    quantidade_de_colunas = len(quadro.colunas)
    assert quantidade_de_colunas == 0

def test_inserir_uma_coluna_deve_existir_uma_coluna(quadro):
    quadro.inserir_colunas(Coluna(nome='A fazer'))
    assert len(quadro.colunas) == 1

def test_quando_inserir_a_coluna_a_fazer_deve_estar_no_quadro(quadro):

    quadro.inserir_colunas(Coluna(nome='Fazendo'))

    assert quadro.colunas[0].nome == 'Fazendo'

def test_quando_inserir_uma_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(quadro):
    quadro.inserir_colunas(Coluna('feito'))
    quadro.inserir_tarefa(Tarefa(nome='Dormir'))
    assert len(quadro.colunas[0].tarefas) == 1

def test_quando_inserir_duas_tarefa_no_quadro_ela_deve_estar_na_primeira_coluna(quadro):
    quadro.inserir_colunas(Coluna('feito'))
    quadro.inserir_tarefa(Tarefa(nome='Dormir'))
    quadro.inserir_tarefa(Tarefa(nome='Comer'))
    assert len(quadro.colunas[0].tarefas) == 2