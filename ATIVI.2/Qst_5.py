'''
Questão 5: Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.
'''

def lista():
    l_1 = []
    for i in range(5):
        num = int(input(f"Numero {i+1}:  "))
        l_1.append(num)
    return l_1

def intercalar_lista(l1, l2):
    juntar = []
    for i in range(len(l1)):
        juntar.append(l1[i])
        juntar.append(l2[i])
    return juntar

#Principal
print("Lista 1")
lista1 = lista()

print("Lista 2")
lista2 = lista()

resultado = intercalar_lista(lista1, lista2)

print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista Intercalada: {resultado}")
