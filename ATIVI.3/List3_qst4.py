'''
Questão 4: Crie uma função chamada "contar_divisores" que receba um número inteiro como
parâmetro e retorne a quantidade de divisores desse número.
'''

def contar_divisores(n1):
    qtd = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            qtd += 1
    return qtd



num = int(input("Digite um numero: "))
while num <=0:
    num = int(input("Não pode ser numero menor que zero. Tente denovo!: "))
    
resultado = contar_divisores(num)
print(f'O numero {num} tem {resultado} divisores!')