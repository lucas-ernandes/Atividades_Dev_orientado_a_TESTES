'''
Questão 14: Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.
'''
max_lista =  10
list_c = []

for i in range(max_lista):
    num = int(input(f"Digite o {i+1}º valor: "))
    list_c.append(num)

print(f"\n{list_c}")

#trocar os 10 valores
for i in range(max_lista):
    if list_c[i] < 0:
        list_c[i] = 0
        
print(f"\nLista C modificada: ", list_c)