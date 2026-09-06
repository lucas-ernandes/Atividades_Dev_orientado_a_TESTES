'''
Questão 15: Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.
'''
max_lista = 5
D = []
E = []

def lista_d():
    for i in range(max_lista):
        sla = input(f"Digite o {i+1}º elemento:")
        D.append(sla)
    return D

def lista_e_inversa():
    for i in range(len(D)-1, -1, -1):
        E.append(D[i])
    return E
        
#Principal
d = lista_d()
e = lista_e_inversa()
print(f"\nLista D: {d}")
print(f"\nLista E (Inversa): {e}")