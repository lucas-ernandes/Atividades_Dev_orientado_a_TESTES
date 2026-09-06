'''Questão 14:  Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.

S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
''' 

def calcular_S(n):
    s = 1
    fatorial = 1

    for i in range(1, n + 1):
        fatorial = fatorial * i
        s = s + 1 / fatorial

    return s


while True:
    n1 = int(input("Digite um numero inteiro positivo: "))

    if n1 > 0:
        break

print(f"O valor S é: {calcular_S(n1):.3f}")