from datetime import datetime


class TimeElapsed:

    def __init__(self):
        self.start_time = datetime.now()
        self.elapsed_time = None

    def finish(self):
        self.elapsed_time = (datetime.now() - self.start_time)



def get_sorted_list(amount):
    return [i for i in range(amount)]

def buscaLinear (busca, lista):
    for i in range(len(lista)):
        if lista[i] == busca:
            return i
    return -1
        

valor = 5040

temporizador = TimeElapsed()
lista = get_sorted_list(100000)
buscaL = buscaLinear(valor, lista)
#print(buscaL)
temporizador.finish()

#if buscaL != -1:
#    print(f"Valor {valor} achado em {buscaL}")

#print(f"Tempo decorrido: {temporizador.elapsed_time}")
#print(f"Quantidade de itens: {len(lista)}")

def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

def recursive_binary_search_a(element_searched, sorted_list):
    center = int(len(sorted_list)/2)
    if sorted_list[center] == element_searched:
        return sorted_list[center]
    if len(sorted_list) == 1:
        return None
    if sorted_list[center] > element_searched:
        recursive_binary_search_a(element_searched, sorted_list[:center])
    else:
        recursive_binary_search_a(element_searched, sorted_list[center:])

def recursive_binary_search_b(element_searched, sorted_list, start=0, end=None):
    if end is None:
        end = len(sorted_list) - 1
        if start > end:
            return None
        center = (start + end) // 2
        current = sorted_list[center]
        if current == element_searched:
            return current
        elif current > element_searched:
            return recursive_binary_search_b(element_searched, sorted_list, start, center - 1)
        else: 
            return recursive_binary_search_b(element_searched, sorted_list, center + 1, end)

#print(busca_binaria(lista, 45345))
#print(busca_binaria(lista, 5455435545))

print(recursive_binary_search_a(7568, lista))
print(recursive_binary_search_b(23423, lista))