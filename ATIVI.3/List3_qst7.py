'''
Questão 7:  Escreva uma função chamada "encontrar_elemento_faltante" que receba uma lista de
números de 1 a n (sendo n um número inteiro) em ordem aleatória, com um elemento
faltando, e retorne o elemento que está faltando. Ex: [4,3,1,5] = 2
'''

def encontrar_elemento_faltante(lista):
    n = len(lista) +1
    soma = 0
    
    for i in range(1, n + 1):
        soma += i
        
    soma_lista = 0
    for num in lista:
        soma_lista += num
        
    return soma - soma_lista

#principal
numero = [1, 3, 4, 5, 6, 2]
print(encontrar_elemento_faltante(numero))