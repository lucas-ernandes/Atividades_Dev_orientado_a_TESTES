'''
Questão 6: 6. Crie uma função chamada "contar_substrings" que receba uma string e uma substring
como parâmetros e retorne a quantidade de ocorrências da substring na string.
'''

def contar_substring(s, ss):
    cont_ss = 0

    for i in range(len(s) - len(ss) +1):
        s1 = ""
        
        for x in range(i, i+len(ss)):
            s1 += s[x]
        print(s1)
        
        if s1 ==  ss:
            cont_ss +=1
            
    return cont_ss

while True:
    texto = input('Digite sua string: ')
    subtexto = input('Digite a substring: ')
    
    if len(subtexto) > len(texto):
        print('O subtexto deve ser menor ou igual o texto!')
        print('Digite novamente!')
    else:
        break

print(f"Existem {contar_substring(texto, subtexto)} ocorrências de  '{subtexto}' no texto '{texto}'")