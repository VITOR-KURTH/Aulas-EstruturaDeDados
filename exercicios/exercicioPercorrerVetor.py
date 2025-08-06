notas = [7.5,8.5,9,4.5,3,6.5,7,1.5,5,10,9.5,7,2,5.5,8,8.5,4.5,6,9,3.5]
nota = 0
while nota != -1:
    soma = 0
    tamanho = len(notas)
    for nota in notas:
        soma += nota
    media = soma/tamanho

    max = notas[0]
    for nota in notas:
        if max < nota:
            max = nota
    print(max)
    nota = int(input("Digite a nota"))
