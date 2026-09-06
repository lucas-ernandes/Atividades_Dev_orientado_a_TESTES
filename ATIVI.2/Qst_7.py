'''
Questão 7: Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um 
outro valor dado pertence ou não à lista
'''
max_lista = 10

def ler_lista():
    l = []
    for i in range(max_lista):
        num = float(input(f"Digite o elemento {i+1}: "))
        l.append(num)
    return l
    
def verificar_pertencimento(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False
    
# Principal
print(f"--- Digite os {max_lista} números da lista ---")
minha_lista = ler_lista()

valor_busca = float(input("\nDigite o valor que deseja buscar: "))

if verificar_pertencimento(minha_lista, valor_busca):
    print(f"O valor {valor_busca} PERTENCE à lista.")
else:
    print(f"O valor {valor_busca} NÃO PERTENCE à lista.")
