'''Questão 10: Escreva uma função chamada "verificar_quadrado_perfeito" que receba um número
inteiro como parâmetro e retorne True se o número for um quadrado perfeito, e False
caso contrário. Um número inteiro é considerado um quadrado perfeito quando ele é o
resultado da multiplicação de um número inteiro por ele mesmo. Em outras palavras, um
número inteiro "n" é um quadrado perfeito se existir um número inteiro "m" tal que "n =
m * m". Por exemplo, os números 4, 9, 16 e 25 são quadrados perfeitos, pois podem ser
obtidos pela multiplicação de um número inteiro por ele mesmo: 4 = 2 * 2; 9 = 3 * 3; 16 =
4 * 4; 25 = 5 * 5.

'''

def verificar_quadrado_perfeito(n):
    if n < 0:
        return False
    
    for i in range(n +1):
        if i * i == n:
            return True
    return False

#Principal

while True:
    try:
        numero = int(input('Digite um numero: '))
        while numero < 0:
            numero = int(input("Numero invalido, tem que ser maior ou igual a 0: "))
            
        if verificar_quadrado_perfeito(numero):
            print(f'{numero} é um quadrado perfeito!')
            break
        else:
            print(f'{numero} não é quadrado perfeito!')
    
    except ValueError:
        print("Não foi possivel verificar o quadrado perfeito!")



''' numero = int(input('Digite um numero: '))

if verificar_quadrado_perfeito(numero):
    print(f' {numero} é um Quadrado Perfeito!')
else:
    print(f'{numero} não é um Quadrado Perfeito!')
    '''