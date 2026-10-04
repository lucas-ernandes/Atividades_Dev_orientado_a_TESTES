'''
Questão 3: Escreva uma função chamada "contar_caracteres" que receba uma string como
parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string
e os valores são a quantidade de ocorrências de cada caractere.
'''

def contar_caracteres(texto):
    qtd_caracteres = {}

    for caractere in texto:
        if caractere in qtd_caracteres:
            qtd_caracteres[caractere] += 1
        else:
            qtd_caracteres[caractere] =  1
            
    return qtd_caracteres

#Principal
texto1 = input("Digite uma palavra: ")

print(f"Seu texto \n{contar_caracteres(texto1)}")