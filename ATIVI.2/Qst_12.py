'''
12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
'''

max_questao = 5

gabarito = []

for i in range(max_questao):

    resposta = input(f"Digite o gabarito da questão {i + 1}: ").upper()

    while resposta not in "ABCDE":

        print("Resposta inválida! Digite apenas A, B, C, D ou E.")

        resposta = input(f"Digite o gabarito da questão {i + 1}: ").upper()

    gabarito.append(resposta)


quantidade_alunos = int(input("Digite o número de alunos: "))


def corrigir_prova():

    numero_aluno = int(input("Digite o número do aluno: "))

    respostas = []

    for i in range(max_questao):

        resposta = input(f"Digite a resposta da questão {i + 1}: ").upper()

        while resposta not in "ABCDE":

            print("Resposta inválida! Digite apenas A, B, C, D ou E.")

            resposta = input(f"Digite a resposta da questão {i + 1}: ").upper()

        respostas.append(resposta)

    acertos = 0

    for i in range(max_questao):

        if respostas[i] == gabarito[i]:
            acertos += 1

    return numero_aluno, acertos


# ===================================
# PRINCIPAL

print(f'''==== GABARITO ====

{gabarito}''')


for i in range(quantidade_alunos):

    numero, acertos = corrigir_prova()

    print(f"Aluno {numero}: {acertos} acertos")

print()