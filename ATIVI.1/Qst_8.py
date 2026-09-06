'''Questão 8: Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
'''

def ler_carcter():
    caractere = input("Deseja continuar? Digite S ou N: ").upper()

    while caractere != "S" and caractere != "N":
        print("\nCaractere inválido. Digite novamente!")
        caractere = input("Deseja continuar? Digite S ou N: ").upper()
        
    return caractere

while True:
    numero = float(input("Digite um número: "))
    print(numero **3)

    if ler_carcter() == "N":
        break