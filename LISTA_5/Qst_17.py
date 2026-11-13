'''
Questão 17 – Cálculo de desconto

Implemente calcular_desconto(valor, percentual), retornando o preço após desconto.
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 50) == 100
'''

def calcular_desconto(valor, percentual):
    if type(valor) != int or type(percentual) != int:
        return Exception
    
    calculo = (valor*percentual) / 100
    desconto = valor - calculo
    return desconto
    

# TESTES
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 50) == 100
assert calcular_desconto('sals', 2) == Exception
assert calcular_desconto('', 9) == Exception
assert calcular_desconto(50, 50) == 25

print('Testes OK!!')