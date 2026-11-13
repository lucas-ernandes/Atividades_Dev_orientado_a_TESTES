'''
Questão 14 – Contar números pares

Implemente contar_pares(numeros), retornando a quantidade de inteiros pares.
assert contar_pares([1, 2, 3, 4, 6]) == 3
assert contar_pares([1, 3, 5]) == 0
'''

def contar_pares(numeros):
    if type(numeros) != list or len(numeros) == 0:
        return Exception
    
    pares =[]

    for i in numeros:
        if i%2 == 0:
            pares.append(i)
    return len(pares)


assert contar_pares([1, 2, 3, 4, 6]) == 3
assert contar_pares([1, 3, 5]) == 0
assert contar_pares([2, 5, 8]) == 2
assert contar_pares('sla1121') == Exception
assert contar_pares([]) == Exception
print('Testes OK!!')