'''
Questão 3:Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.
'''

max_list = 4
l = list(range(max_list))
qtd = 0

for i in range(max_list):
    l[i] = int(input("Digite uma sequencia de numeros: "))
    qtd += l[i]

inverter = l[::-1]

print(f"Lista: {l}")
print(f"Lista invertida: {inverter}")