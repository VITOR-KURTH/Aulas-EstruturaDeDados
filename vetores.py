from random import random

#notas_alunos = [7.5, 8.0, 6.5]

#len(notas_alunos)

#print(notas_alunos[-1])

#print("------")

#for notas in notas_alunos:
#    print(notas)

#print("------")

#for indice in range(len(notas_alunos)):
#    print(notas_alunos[indice])

notas = []
nota = 0
while nota != -1:
    nota = float(input("Escreva a sua nota (-1 para sair):"))
    if nota != -1:
        notas.append(nota)

for i in notas:
    if i > 7:
        print(i)

