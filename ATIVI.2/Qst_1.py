"""Lista2_q1) Faça um programa em python que tenha: 	
a) Uma função para criar/gravar uma lista com 100 elementos numéricos inteiros;
b) Uma função para mostrar a quantidade de números pares e números ímpares; 
c) Uma função para gerar duas outras listas, uma lista somente com os números
   pares da lista original e outra lista somente com os números ímpares;
d) Função para mostrar o maior elemento da lista original;
e) Mostrar as 3 listas no programa principal. """

max_lista = 10
l = list(range(max_lista))
l_p = []
l_i = []
from random import *

#a)
def gravar_lista():
    for i in range (max_lista):
        l[i] = randint(-100,100)   #     gera números inteiros aleatórios
    return l
#b)
def quant_p_i():
    cont_par = 0
    cont_impar = 0
    for i in range (max_lista):
        if l[i] % 2 == 0:
           cont_par += 1    
        else:
           cont_impar += 1
           
    return cont_par, cont_impar

#c)
def gerar_duas_listas():
    for i in range (max_lista):
        if l[i] % 2 == 0:
           l_p.append(l[i])    
        else:
           l_i.append(l[i])
           
    return l_p, l_i

#d)
def maior():
    maior = l[0]
    for i in range (1,max_lista):
        if l[i] > maior:
           maior = l[i]
    return maior

#Principal
lista = gravar_lista()

pares, impares = quant_p_i()

lista_pares, lista_impares = gerar_duas_listas()

maior_numero = maior()

# e)
print("Lista L:", lista)
print("\nQuantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
print("\nMaior número da lista L:", maior_numero)
print("\nPares :", lista_pares)
print("Ímpares :", lista_impares)