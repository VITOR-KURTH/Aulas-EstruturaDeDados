from dataclasses import dataclass
import random



@dataclass
class Carta:

    def __init__(self):
        self.atk = random.randint(1, 6)
        self.defe = random.randint(3, 13)
        self.vel = random.randint(1, 10)



#fila = mao 4 cartas
#pilha = bolo de cartas

#Pilha
class PilhaCartas:
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



pilhaJogador = PilhaCartas()
pilhaOponente = PilhaCartas()

for carta in range(10):
    pilhaJogador.push(Carta())
    pilhaOponente.push(Carta())
print(f"Tamanho pilhas:\nJog:{len(pilhaJogador.baralho)}, Op:{len(pilhaOponente.baralho)}")

filaDeckJog = []
filaDeckOp = []

while pilhaJogador.size() > 6:
    cartaPegada = pilhaJogador.pop(0)
    filaDeckJog.append(cartaPegada)

while pilhaOponente.size() > 6:
    cartaPegada = pilhaOponente.pop(0)
    filaDeckOp.append(cartaPegada)
print(len(filaDeckJog))
print(len(filaDeckOp))






