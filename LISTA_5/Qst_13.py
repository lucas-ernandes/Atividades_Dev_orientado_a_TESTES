'''
Questão 13 – Remover duplicados
Implemente remover_duplicados(lista), preservando a ordem da primeira ocorrência.

assert remover_duplicados([1, 2, 2, 3]) == [1, 2, 3]
assert remover_duplicados([5, 5, 5]) == [5]
'''

def remover_duplicados(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
        
    duplicado = []
    for i in lista:
        if i not in duplicado:
            duplicado.append(i)
    return duplicado

assert remover_duplicados([1, 2, 2, 3]) == [1, 2, 3]
assert remover_duplicados([5, 5, 5]) == [5]
assert remover_duplicados('sla') ==  Exception
assert remover_duplicados([]) == Exception
assert remover_duplicados([1.3, 2.5, 9,5]) == [1.3, 2.5, 9,5]
assert remover_duplicados([1,2,3,5,5, 6, 7,7]) == [1,2,3,5,6,7]

print('Testes OK!!')