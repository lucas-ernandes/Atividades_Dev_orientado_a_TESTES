'''
17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.
'''

max_lista = 10

W = []
posicoes = []

def lista_W():
    for i in range(max_lista):
        num = input(f"Digite o {i+1}º elemento: ")
        W.append(num)
    return W


def achar_v(v):
    contador = 0
    for i in range(len(W)):
        if W[i] == v:
            contador += 1
            posicoes.append(i)
    return contador
        
#principal
print(f"==== ESCREVA {max_lista} ELEMENTOS ====")

w = lista_W()

v = input("\nQual elemento quer achar?: ")

resultado = achar_v(v)

if resultado == 0:
    print(f"\nO valor {v} não aparece na lista.")
else:
    print(f'\nO valor {v} aparece {resultado} vezes.')
    print(f"\nEle parece nas posição: {posicoes} ")
    
print(f"\nLista W: {w}")