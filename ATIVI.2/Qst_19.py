'''
19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.
'''
max_list_R = 5
max_list_S = 10

R = []
S = []

def lista_R():
    for i in range(max_list_R):
        num = int(input(f"Digite o {i+1}º elemento da Lista R: "))
        R.append(num)
    return R

def lista_S():
    for i in range(max_list_S):
        num = int(input(f"Digite o {i+1}º elemento da Lista S: "))
        S.append(num)
    return S

def juntar_lista():
    lista_x = R + S
    
    return lista_x


print(f'==== Digite {max_list_R} elementos da Lista R')
ler_R = lista_R()
print(f'\nLista R: {ler_R}')

print(f'\n\n==== Digite {max_list_S} elementos da Lista S')
ler_S = lista_S()
print(f'\nLista S: {ler_S}')

print("\n==== Lista X SUPREMA ====")
lex_X = juntar_lista()
print(f'\nLista X: {lex_X}')