from dataclasses import dataclass
import random

def dado():
    """Função que retorna soma de dois dados de seis lados"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

@dataclass
class Carta:
    """Cria o objeto carta com atributos: atk, defe, vel"""
    def __init__(self):
        self.atk = random.randint(1, 6)
        self.defe = random.randint(3, 12)
        self.vel = random.randint(1, 10)



#fila = mao 4 cartas
#pilha = bolo de cartas

#Pilha
class PilhaCartas:
     """"Cria a pilha para cartas, no caso o bolo de cartas"""
     def __init__(self):
         self.baralho = []

     def push(self, carta):
         self.baralho.append(carta)

     def pop(self):
         return self.baralho.pop(-1)

     def peek(self):
         return self.baralho[len(self.baralho)-1]

     def size(self):
         return len(self.baralho)

class FilaCartas:
    """Cria a fila para cartas, no caso a mão de cartas"""
    def __init__(self):
        self.deck = []

    def isEmpty(self):
        return self.deck == []

    def enqueue(self, deck):
        self.deck.insert(0,deck)

    def dequeue(self):
        return self.deck.pop()

    def size(self):
        return len(self.deck)


pilhaJogador = PilhaCartas()
pilhaOponente = PilhaCartas()

for carta in range(10):
    pilhaJogador.push(Carta())
    pilhaOponente.push(Carta())
print(f"Tamanho pilhas:\nJog:{len(pilhaJogador.baralho)}, Op:{len(pilhaOponente.baralho)}")

filaDeckJog = FilaCartas()
filaDeckOp = FilaCartas()

while pilhaJogador.size() > 5:
    cartaPegada = pilhaJogador.baralho.pop()
    filaDeckJog.enqueue(cartaPegada)

while pilhaOponente.size() > 5:
    cartaPegada = pilhaOponente.baralho.pop()
    filaDeckOp.enqueue(cartaPegada)

print("Deck jogador:",len(filaDeckJog.deck))
print("Deck oponente:",len(filaDeckOp.deck))

print("Valor dado",dado())

