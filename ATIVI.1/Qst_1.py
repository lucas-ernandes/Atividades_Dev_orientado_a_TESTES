'''Questão 1: 1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
'''

def par_impar(n):
    if n % 2 ==0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par_impar(num):
    print(f'O numero {num} é PAR! ')
else:
    print(f'O numero {num} é IMPAR! ')