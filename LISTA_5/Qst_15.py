'''
Questão 15 – Segundo maior elemento

Implemente segundo_maior(numeros), retornando o segundo maior valor distinto.
assert segundo_maior([3, 8, 5, 10]) == 8
assert segundo_maior([10, 10, 8, 5]) == 8
'''
def segundo_maior(numero):
    if type(numero) != list or len(numero) == 0:
        return Exception
    for i in numero:
        if type(i) != int:
            return Exception
        
    v_2 = []
    for i in numero:
        if i != max(numero):
            v_2.append(i)

    return max(v_2)

#TESTES
assert segundo_maior([3, 8, 5, 10]) == 8
assert segundo_maior([10, 10, 8, 5]) == 8
assert segundo_maior([]) == Exception
assert segundo_maior(['sla kkkkk']) == Exception
assert segundo_maior([2, 9, 10, 'www']) == Exception

print('Testes OK!!!')