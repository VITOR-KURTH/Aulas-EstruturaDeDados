class Aluno:
    def __init__(self, nome: str, idade: int, media: float):
        self.nome = nome
        self.idade = idade
        self.media = media
    def aprovado(self):
        if self.media >= 7.0:
            return "aprovado"
        return "reprovado"

aluno = Aluno("Vitor",18,8)

print(aluno.aprovado())