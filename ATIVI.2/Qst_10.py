
'''
Questão 10: Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.
'''


max_list = 15
l = []

for i in range(max_list):
    num = int(input(f"Digite o {i+1}º elemento: "))
    l.append(num)

def maior():
    maior = l[0]

    for i in range (1, max_list):
        if l[i] > maior:
            maior = l[i]
    return maior

def menor():
    menor = l[0]

    for i in range(1, max_list):
        if l[i] < menor:
            menor = l[i]
            
    return menor

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
print(f"\nO MAIOR numero da lista é: {maior()} na posição: {pos_maior}")
print(f"\nO MENOR numero da lista é: {menor()} na posição: {pos_menor}")