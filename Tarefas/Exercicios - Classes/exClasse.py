from dataclasses import dataclass

sair = 0

while sair != 1:
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

    livros = []
    def AdicionaLivro():
        quantidade = int(input("Quantos livros:"))
        for i in range(quantidade):
            nome = input(f"Digite o nome {i}:")
            autor = input(f"Digite o autor {i}:")
            ano = int(input(f"Digite o ano {i}:"))
            preco = float(input(f"Digite o preço {i}:"))

            livro = Livro(nome, autor, ano, preco)

            livros.append(livro)

    AdicionaLivro()
    print(livros)
    
    caro(livros)

    sair = int(input("Sair?(1): "))

        