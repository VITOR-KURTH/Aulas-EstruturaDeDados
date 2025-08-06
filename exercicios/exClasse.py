from dataclasses import dataclass

@dataclass
class Livro:
    Titulo: str
    Autor: str
    Ano: int
    Preco: float
    def recente(self):
        if self.Ano > 2020:
            return True
        return False
    
    def caro(self):
        soma = 0
        tamanho = len(livros)
        for livro in livros:
           soma += livro.Preco
        media = soma/tamanho
        if self.Preco > media:
            return "Caro"
        return "Barato"


livro1 = Livro("Do but ao sigma", "Gabriel", 2015, 55.5)
livro2 = Livro("Frango do G: a historia", "Pedro", 2025, 40.3)
livro3 = Livro("Eu sou o imbroxavel", "Bolsonaro", 2024, 100.22)
livro4 = Livro("500 dias de falta", "Guilherme", 2019, 32.1)

livros = [livro1, livro2, livro3, livro4]

print(livro1.recente())
print(livro1.caro())


        