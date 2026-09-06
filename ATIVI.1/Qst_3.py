'''Questão 3: 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5
'''

def celsius(f):
    return ((f-32)/9)*5

f = float(input('Digite a temperatura em Fahrenheit: '))
print(f'Temperatura em Celsius(C): {celsius(f):.2f}')