'''
Questão 3:Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.
'''

n = int(input("Digite a sequencia de numeros desejados: "))
l = list(range(n))

def lista_normal():
    for i in range(n):
        l[i] = int(input("Digite uma sequencia de numeros: "))
    return l

def lista_inverti():
    l2 = []
    for x in range(n-1, -1, -1):
        l2.append(l[x])
        
    return l2

resultado = lista_normal()
resultado2 = lista_inverti()

print(f"Lista: {resultado}")
print(f"Lista invertida: {resultado2}")