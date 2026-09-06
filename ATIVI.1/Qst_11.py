'''Questão 11: Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
'''
def num_divisor(n1):
    qtd = 0
    
    for i in range(1, n1 +1):
        if n1 % i == 0:
            qtd += 1
    return qtd

while True:
    try:
        n1 = int(input("Digite um numero inteiro para ver seus divisores: "))

        while n1 <= 0:
            n1 = int(input("Numero negativo não pode! Somente positivo(>0), tente novamente: "))
    
        print(f"O numero {n1} tem {num_divisor(n1)} divisores")

    except ValueError:
        print("Número inválido. Digite apenas números inteiros.")
        break