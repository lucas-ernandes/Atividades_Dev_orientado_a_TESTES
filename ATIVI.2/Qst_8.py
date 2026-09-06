'''
Questão 8: Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.
'''

max_letras = 5
l= []

def contar_letras():
    for i in range(max_letras):
        letra = input("Digite uma letra: ")

        while len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra!")
            letra = input("Digite uma letra: ")

        l.append(letra.upper())

    contador = 0

    for letra in l:
        if letra == "A":
            contador += 1

    return contador
#principal
contador = contar_letras()
print(l)
print(f"A letra 'A' apareceu {contador} vezes. ")
       
        
