'''Questão 12: 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
'''

def somatorio(n1):
    soma = 0
    
    for i in range(1, n1 + 1):
        soma += i
    return soma

n1 = int(input("Digite um numero inteiro: "))
print(f"O somatório do numero {n1} é {somatorio(n1)}")