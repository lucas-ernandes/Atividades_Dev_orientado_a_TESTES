'''
Questão 2: Crie uma função chamada "verificar_anagrama" que receba duas strings como
parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as
mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário.
'''

def verificar_anagrama(a, b):
    palavra1 = a.lower()
    palavra2 = b.lower()

    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False
    
    
#Principal
text1 = input("Digite a 1º palavra: ")
text2 = input("Digite a 2º palavra: ")

print(verificar_anagrama(text1, text2))