'''
Questão 5:  Escreva uma função chamada "verificar_ano_bissexto" que receba um número inteiro
como parâmetro e retorne True se o ano for bissexto, e False caso contrário. Um ano é
bissexto se for divisível por 4, mas não divisível por 100, exceto se for divisível por 400.
'''

def verificar_ano_bissexto():
    ano = int(input('Digite um ano: '))
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        return 'Ano bissexto!'
    else:
        return 'Não é bissexto!'

#principal
resultado = verificar_ano_bissexto()
print(resultado)