from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    media: float

aluno = Aluno("Vitor", 18, 9.5)

print(aluno.nome, aluno.idade)