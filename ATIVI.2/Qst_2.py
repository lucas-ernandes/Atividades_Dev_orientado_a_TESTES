'''
Questão 2: Faça um programa que grave uma lista com dez números reais, 
calcule e mostre a quantidade de números negativos e a soma 
dos números positivos dessa lista.
'''

from random  import *

max_list = 10
l = list(range(max_list))

qtd_negativa = 0
soma_posit = 0.0

for i in range(max_list):
    l[i] = round(randint(-100, 100), 2)
    if l[i] < 0:
        qtd_negativa += 1
    else:
        soma_posit +=l[i]

print("Lista: ",l)
print(f"Qtd de numeros negativos: {qtd_negativa}")
print(f"Soma dos números: {soma_posit:.2f}")