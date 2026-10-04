def soma(n1, n2):
    soma_numeros = 0
    for i in range(n1, n2+1):
        soma_numeros +=i
    return soma_numeros
while True:
    try:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
        while n1 and n2 <0:
            n1 = int(input('Não aceita valores menor que zero'))
            n2 = int(input('Não aceita valores menor que zero'))
        print(f'A soma dos numeros é {soma(n1, n2)}')
        break
    except ValueError:
        print('Não aceitar valores estranhos!')