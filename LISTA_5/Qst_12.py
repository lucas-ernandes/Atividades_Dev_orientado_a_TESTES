'''
Questão 12 – Média de uma lista
Implemente calcular_media(numeros).

assert calcular_media([8, 6, 10]) == 8
assert calcular_media([5, 5, 5]) == 5
'''

def calcular_media(numeros):
    for i in numeros:
        if type(i) == str or i < 0:
            return Exception
    
    
    soma_total = 0
    
    for i in numeros:
        soma_total += i
        
    quantidade = len(numeros)
    media = round(soma_total // quantidade, 2)
    
    return media

assert calcular_media([8, 6, 10]) == 8
assert calcular_media([5, 4, 8, 7]) == 6
assert calcular_media([9, 10, 'seila', 7]) == Exception
assert calcular_media([8.3, 9, 3]) == 6
assert calcular_media([-2, -4, 3.3]) == Exception

print("Testes OK!!")