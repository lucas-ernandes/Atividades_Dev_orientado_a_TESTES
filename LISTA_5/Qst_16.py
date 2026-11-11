'''
Questão 16 – Situação do aluno

Implemente situacao_aluno(nota): Aprovado para nota ≥ 7; Recuperacao para 4 ≤ nota < 7; Reprovado para nota < 4.
assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(5) == "Recuperacao"
'''
def situacao_aluno(nota):
    if type(nota) == str or type(nota) == list:
        return Exception
    
    if nota >= 7:
        return 'Aprovado'
    elif nota >=4:
        return 'Recuperacao'
    else:
        return 'Reprovado'

# TESTES
assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(5) == "Recuperacao"
assert situacao_aluno(3) == "Reprovado"
assert situacao_aluno('') == Exception
assert situacao_aluno('www') == Exception
assert situacao_aluno(1.2) == 'Reprovado'
assert situacao_aluno([1.2, 2]) == Exception

print('TESTES OK!!!')