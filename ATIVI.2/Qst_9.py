'''
Questão 9: Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
'''

max_list = 5
X = []
Y = []

for i in range(max_list):
    num = int(input("Digite um numero: "))
    X.append(num)

for i in range(len(X) -1, -1, -1):
    Y.append(X[i])

print(f'\nLista X: {X}')
print(f'\nLista Y: {Y}')