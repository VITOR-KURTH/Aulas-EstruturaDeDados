#Criação do dicionário:
log_de_viagens = {
    #Continente
    "Europa": {
        #Pais     #Cidades
        "França": ["Paris", "Merselles", "Lyon"],
        "Alemanha": ["Berlin", "Frankfurt", "Hamburgo"]
    },
    "America": {
        "Estados Unidos": ["Nova Iorque", "Dallas", "Los Angeles"],
        "Brasil": ["Brasilia", "Rio de Janeiro", "São Paulo"],
    },
    "Africa": {

    },
    "Asia": {
        "Japão": ["Tokyo", "Kyoto", "Osaka"],
        "China": ["Pequin", "Beijin", "Shangai"]
    }
}

#Incluir na key "Africa" um país: "Africa do sul" e a lista de cidades
log_de_viagens["Africa"] = {
    "Africa do Sul": ["Joanesburgo", "Cidade do Cabo", "Pretória"]
}

#Printar todo o dicionário
print(log_de_viagens)

#Percorrer os continentes no dicionário
for continentes in log_de_viagens:
    print("Continente:",continentes)
    #Percorrer países no dicionário com a key continentes
    for paises in log_de_viagens[continentes]:
        print("-----------------------")
        print("-País:", paises)
        #Percorrer cidades  no dicionário com a key continentes e paises
        for cidades in log_de_viagens[continentes][paises]:
            print("Cidade",cidades)
    print("=============================")

def adicionaViagem(continente, pais, cidade):
    
    continente = log_de_viagens[continente] = {

    }
    pais = log_de_viagens[continente] = {
        pais
    }
    cidade = log_de_viagens[continente] = {
        pais: cidade
    }

continente = input("Digite o continente: ")
pais = input("Digite o pais: ")
cidade = input("Digite a cidade: ")

adicionaViagem(continente, pais, cidade)