"""
Questão 11: – Maior elemento de uma lista

Implemente maior_lista(numeros) para uma lista numérica não vazia.
assert maior_lista([3, 8, 2, 10]) == 10
assert maior_lista([-5, -2, -9]) == -2
"""

def maior_lista(numeros):
    for i in numeros:
        if type(i) != int:
            return Exception
    
    maior = numeros[0]

    for i in numeros:
        if i > maior:
            maior = i
    return maior

assert maior_lista([3, 8, 2, 10]) == 10
assert maior_lista([-5, 2, -9]) == 2
assert maior_lista([2, 'sla', 2.3, 5]) == Exception
assert maior_lista([2, '', 2.9, 10]) == Exception
assert maior_lista([-909, 0, -1, -5]) == 0

print("Testes OK!!")

    
        