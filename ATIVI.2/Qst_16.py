'''
16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.
'''

max_lista = 10
X = []
Y = []

#X
def lista_x ():
    for i in range(max_lista):
        num = int(input(f"Digite o {i+1}ª elemento: "))
        X.append(num)
    return X

#Y
def lista_y():
    for i in range(max_lista):
        
        if i % 2 == 0:
            Y.append(X[i] / 2)
        else:
            Y.append(X[i] * 3)
    return Y

x = lista_x()
y = lista_y()
print(f'\nLista X:\n {x}')
print(f'\nLista Y:\n {y}')