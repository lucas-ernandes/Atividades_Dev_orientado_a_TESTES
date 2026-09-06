'''QUestão 15: 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
'''

def calcular_S(n):
   s =0 
   for i in range(1, n + 1):
       s = s + (i**2 + 1) / (i+3) 
       
   return s

while True:
    n1 = int(input("Digite um numero inteiro positivo: "))

    if n1 > 0:
        break

print(f"O valor S é: {calcular_S(n1):.2f}")  