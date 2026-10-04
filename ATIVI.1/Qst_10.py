'''Questão 10:  Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
deles;
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
Max.'''

def Max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
for i in range(4):
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    n3 = int(input("Digite o terceiro numero: "))
    n4 = int(input("Digite o quarto numero: "))
    
    maior = Max(n1, n2)
    maior = Max(maior, n3)
    maior = Max(maior, n4)
    
    print(f"O maior número é: {maior}")
