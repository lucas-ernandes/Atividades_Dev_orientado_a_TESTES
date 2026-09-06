'''
Questão 13: Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.
'''

dado_resultado = []

def contar_face(resultado, face):
    contador = 0
    
    for vezes in resultado:
        if vezes == face:
            contador += 1
    return contador

#Principal
n = int(input("Quantos lançamentos: "))

for i in range(n):
    resultado = int(input("Resultado: "))
    dado_resultado.append(resultado)
    
for face in range(1, 7):
    qtd = contar_face(dado_resultado, face)

    print(f"Face {face}: {qtd} ocorrencias!")
