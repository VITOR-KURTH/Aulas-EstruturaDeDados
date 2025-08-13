# Exercicio filas
# Implemente uma fila para atendimento
# Simule clientes chegando e sendo atendidos
# Mostre o estado da fila após cada operação
# Cliente: Nome, protocolo, hora de chegada, de atendimento, de saida
# Metodo: Caixa Fila
# def atendimento
# def entrada fila
# mostrar estado
# simular entrada e saida de clientes
# chegada de cliente 2s
# tempo de atendimento 10s


from dataclasses import dataclass
from datetime import datetime, timedelta

sair = 0
clientes = [
    "Ana Silva",
    "Bruno Souza",
    "Carla Ferreira",
    "Diego Oliveira",
    "Elisa Martins",
    "Felipe Rocha",
    "Gabriela Lima",
    "Henrique Alves",
    "Isabela Costa",
    "João Mendes",
    "Karen Barbosa",
    "Lucas Ribeiro",
    "Mariana Gomes",
    "Nicolas Faria",
    "Olívia Pires",
    "Paulo Cardoso",
    "Quitéria Andrade",
    "Rafael Teixeira",
    "Sofia Cunha",
    "Tiago Moreira",
    "Úrsula Bezerra",
    "Victor Nunes",
    "Wesley Araújo",
    "Xavier Prado",
    "Yasmin Duarte",
    "Zeca Tavares",
    "Alice Monteiro",
    "Bernardo Freitas",
    "Camila Araújo",
    "Daniel Correia"
]

doisSeg = timedelta(seconds=2)
dezSeg = timedelta(seconds=10)
agora = datetime.now()

while sair != 1:
    def entradaFila():
        if datetime.now() >= agora + doisSeg:
            fila_clientes = []
            for cliente in clientes:
                fila_clientes.append(cliente)
        return fila_clientes
    
    def atendimento(fila_clientes):
        if datetime.now() >= agora + dezSeg:
            clientes_atendimento = []
            for cliente in fila_clientes:
                clientes_atendimento.append(cliente)
        return clientes_atendimento
         
    def saidaAtendimento(clientes_atendimento):
        if datetime.now() >= agora + dezSeg:
            atendido = clientes_atendimento.pop(0)
            print("Cliente atendido:", atendido)

    entradaFila()
    atendimento(fila_clientes)
    saidaAtendimento()
    sair = 0
