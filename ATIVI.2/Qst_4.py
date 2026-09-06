'''
Questão 4: Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.
'''

from random import *

max_list = 15
l = list(range(max_list))

for i in range(max_list):
    l[i] = randint(1, 100)

#a)
def maior():
    maior = l[0]
    
    for i in range (1, max_list):
        if l[i] > maior:
            maior = l[i]
    return maior
#b)
def menor():
    menor = l[0]

    for i in range (1, max_list):
        if l[i] < menor:
            menor = l[i]
    return menor
#encontrar a posição do referente numero
def posicao():
    pos_maior = 0
    pos_menor = 0
    for i in range(len(l)):
        if l[i] == maior():
            pos_maior = i

        if l[i] == menor():
            pos_menor = i
    return pos_maior, pos_menor

#principal
pos_maior, pos_menor = posicao()
print(l)
print(f"\nO MAIOR numero da lista é: {maior()} e está na posição {pos_maior}")
print(f"\nO MENOR número da lista é: {menor()} e está na posição {pos_menor}")