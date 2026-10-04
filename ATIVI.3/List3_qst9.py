'''Questão 9: Escreva uma função chamada "encontrar_elemento_repetido" que receba uma lista de
números como parâmetro e retorne o elemento que se repete mais vezes na lista.
'''

from random import*

max_list = 20
l =list(range(max_list))

def gravar_lista():
    for i in range(max_list):
        l[i] = randint(1, 10)

def encontrar_elem_repetido():
    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    maior_qtd = 0; valor = 0
    for i in dic:
        if dic[i] > maior_qtd:
            maior_qtd = dic[i]
            valor = i
    return valor, maior_qtd

gravar_lista()
print(l)
valor, qtd = encontrar_elem_repetido()
print(f'O valor que mais aparece é {valor}. Aparece {qtd} vezes.')  
