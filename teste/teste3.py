def verificar_quadrado(n):
    for i in range(1, n+1):
        if i * i == n:
            return True
    return False
        
        
num = int(input('Digite um numero: '))
if verificar_quadrado(num):
    print(f'O numero {num} é um quadrado perfeito!')
else:
    print(f'Não é quadrado perfeito!')