'''
Questão 1: Crie uma função chamada "encontrar_primos_gemeos" que receba um número inteiro
n como parâmetro e retorne uma lista contendo todos os pares de números primos
gêmeos menores que n. Os números primos gêmeos são dois números primos
consecutivos que diferem em 2.
'''

def encontrar_primos_gemeos(n):
    l = []
    
    for i in range(2, n):
        primo1 = True
        #verifica se i é primo
        for x in range(2, i):
            if i % x == 0:
                primo1 == False
                break
        
        #Verifica se  i+2 é primo
        primo2 = True
        
        for x in range(2, i+2):
            if (i+2) % x  == 0:
                primo2 = False
                break
            
        # Se os dois forem primos, saõ primos gemeos
        if primo1 and primo2 and i + 2 < n:
            l.append((i, i + 2))
    return l

#Principal
n = int(input("Digite um numero: "))

resultado =  encontrar_primos_gemeos(n)
print(resultado)