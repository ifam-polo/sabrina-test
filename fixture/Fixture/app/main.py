from dataclasses import dataclass

@dataclass
class Tarefa:
    nome: str

class Coluna:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def insere_tarefa(self, tarefa):
        ...

    def __repr__(self):
        return f'Coluna(tarefas={self.tarefas})'

class Quadro:
    def __init__(self, colunas=[]):
        self.colunas = colunas
    def inserir_colunas(self, coluna):
        self.colunas.append((coluna))

    def inserir_tarefa(self, tarefa):
        self.colunas[0].insere_tarefa(tarefa)

    def __repr__(self):
        return f'Quadro(colunas={self.colunas}'

