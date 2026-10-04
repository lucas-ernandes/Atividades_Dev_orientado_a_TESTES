'''8. Crie uma função chamada "remover_vogais" que receba uma string como parâmetro e
retorne uma nova string sem as vogais.
'''

def remover_vogais(vogal):
    palavra_sem_vogal = ""
    for i in vogal:
        if i not in 'aeiou':
            palavra_sem_vogal += i
    
    return palavra_sem_vogal

palavra = input("Digite uma palavra: ").lower()

print(remover_vogais(palavra))
