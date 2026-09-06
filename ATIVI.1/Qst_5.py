'''Questão 5:  Faça um programa que leia a altura e o sexo (codificado da seguinte forma: (1:feminino 2:masculino) de uma pessoa. 
Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
'''

def peso_ideal(sexo, h):
   if sexo == 1:
       return (62.1*h) - 44.7
   else:
       return (72.7*h) - 58

while True:
    try:
        sexo = int(input("Qual o seu sexo - 1:feminino & 2:masculino: "))
        while sexo < 1 or sexo > 2:
            sexo = int(input("Informe apenas 1 ou 2! Tente novamente: "))

        h = float(input("Informe sua altura: "))
        print(f"\nSeu peso ideal seria: {peso_ideal(sexo, h):.2f}")
        break
    
    except ValueError:
        print("Não foi possivel indentificar seu peso ideal!!")