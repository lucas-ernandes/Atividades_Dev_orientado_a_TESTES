def contar_divi(n):
    divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisores +=1
    return divisores

while True:
    try:
        num = int(input('Digite um numero para ver os seus divisores: '))
        while num <=0:
            num = int(input('Digite novamente: '))
            
        print(f'O numero {num} tem {contar_divi(num)} divisores!')
        break
    except:
        print('Não aceita esse valor ai não parceiro')
        break