"""Questão 9:  Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros
contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma. Obs: não aceitar
números inválidos. Obs: n1 deve ser menor que n2."""

def soma_int(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma

while True:
    try:
        n1 = int(input("Digite o 1° numero inteiro: "))
        n2 = int(input("Digite o 2° numero inteiro: "))
        if n1 <= n2:
            print(f"A soma dos numeros é {soma_int(n1, n2)}") 
            break
        else:
            print("O segundo numero deve ser maior que o 1° numero! Tente novamente!")
    except ValueError: 
        print("Numero invalido. tente novamente!")