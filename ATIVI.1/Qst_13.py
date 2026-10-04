'''13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
'''

def calcular_S(n):
    
    s = 0
    for i in range(1, n + 1):
        s = s + 1/i
    return s

while True:
    n1 = int(input("Digite um numero inteiro: "))

    if n1 >0 :    
        print(f"O valor S é: {calcular_S(n1):.2f}")
        break