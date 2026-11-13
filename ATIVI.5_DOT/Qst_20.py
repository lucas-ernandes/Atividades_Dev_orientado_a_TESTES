'''
Questão 20 – Frequência de palavras em um texto

Desenvolva uma função contar_ocorrencias(texto, palavra) que retorne quantas vezes uma palavra aparece em um
texto. A comparação deve ignorar maiúsculas e minúsculas e desconsiderar sinais de pontuação. Conte apenas
palavras completas, e não partes de outras palavras. Se o texto estiver vazio ou a palavra não existir, retorne zero.
Elabore no mínimo cinco testes utilizando assert, incluindo repetições, pontuação, diferença entre maiúsculas e
minúsculas e ausência da palavra.

assert contar_ocorrencias("Python é ótimo. Eu estudo Python!", "python") == 2
assert contar_ocorrencias("Casa, casa; CASA!", "casa") == 3
assert contar_ocorrencias("casamento e casa", "casa") == 1
assert contar_ocorrencias("Aprender programação", "teste") == 0
assert contar_ocorrencias("", "python") == 0
'''

def contar_ocorrencias(texto, palavra):
    if texto == '' or palavra == '':
        return 0
    
    texto = texto.lower()
    palavra = palavra.lower()

    texto = texto.replace('.', '')
    texto = texto.replace(',', '')
    texto = texto.replace('!', '')
    texto = texto.replace('?', '')
    texto = texto.replace(';', '')
    texto = texto.replace(':', '')

    palavras = texto.split()

    contador = 0
    
    for p in palavras:
        if p == palavra:
            contador += 1

    return contador

# TESTES
assert contar_ocorrencias("Olá, mundo! Olá novamente.", "olá") == 2
assert contar_ocorrencias("casamento e casa", "casa") == 1
assert contar_ocorrencias("GATO gato Gato", "gato") == 3
assert contar_ocorrencias("Hoje está bonito", "chuva") == 0
assert contar_ocorrencias("", "python") == 0

print('Testes OK!!!')