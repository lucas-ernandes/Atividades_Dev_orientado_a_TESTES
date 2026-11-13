'''
Implemente validar_cpf(cpf), conferindo os dois dígitos verificadores. Aceite CPF com ou sem pontuação e rejeite
sequências de dígitos iguais.

assert validar_cpf("529.982.247-25") == True
assert validar_cpf("111.111.111-11") == False
'''

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    if not cpf.isdigit() or len(cpf) != 11:
        return False
    
    if cpf == cpf[0]*11:
        return False
    
    # calculo do primeiro digito
    soma =0
    for i in range(9):
        soma += int(cpf[i]) * (10-i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - resto
        
    if digito_1 != int(cpf[9]):
        return False
    
    # Calculo do segundo digito
    
    soma = 0
    
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - resto
        
    if digito_2 != int(cpf[10]):
        return False
    
    return True

#TESTES
assert validar_cpf("529.982.247-25") == True
assert validar_cpf("111.111.111-11") == False
assert validar_cpf("52998224725") == True
assert validar_cpf("12345678900") == False
assert validar_cpf("123") == False


print('TESTES OK!!')