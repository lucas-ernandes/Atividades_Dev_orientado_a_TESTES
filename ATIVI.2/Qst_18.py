'''
QUestão 18: Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
'''

max_lista = 4
X = []
R = []

def lista_x():
    for i in range(max_lista):
        num = int(input(f"Digite o {i+1}º elemento: "))
        X.append(num)
    return X

def copiar():
    for i in range(len(X)):
        if X[i] < 0:
            R.append(X[i])
            
    return R

#principal
print(f"==== ESCREVA {max_lista} ELEMENTOS ====")
x = lista_x()
r = copiar()

print(f'Lista  X: {x}')
print(f'\nLista R:  {r}')