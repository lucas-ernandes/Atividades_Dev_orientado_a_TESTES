'''Questão 2: Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r;
'''

def area(r):
    return 3.14 * r**2

def peri(r):
    return 3.14 * 2 * r

raio = float(input('Raio do circulo: '))

print(f'A area do ciculo é: {area(raio):.2f}')
print(f'O perimetro do circulo é: {peri(raio):.2f}')