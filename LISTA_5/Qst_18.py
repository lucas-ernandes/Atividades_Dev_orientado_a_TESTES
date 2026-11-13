'''
Questão 18 – Cálculo de frete

Implemente calcular_frete(peso, distancia): R$ 10 fixos + R$ 2 por kg + R$ 0,50 por km. Rejeite entradas negativas.
assert calcular_frete(5, 20) == 30
assert calcular_frete(0, 0) == 10
'''
def calcular_frete(peso, distancia):
    if type(peso) not in(int, float) or type(distancia) not in (int, float):
        return Exception
    
    if peso <0 or distancia <0:
        return Exception
    
    calculo_1 = peso * 2
    calculo_2 = distancia * 0.50
    
    frete = calculo_1 + calculo_2 + 10
    
    return frete

# TESTES
assert calcular_frete(5, 20) == 30
assert calcular_frete(0, 0) == 10
assert calcular_frete(-2, 'sal') == Exception
assert calcular_frete('kkk', 'sal') == Exception
assert calcular_frete(10, 20.5) == 40.25

print('Testes OK!!!')

