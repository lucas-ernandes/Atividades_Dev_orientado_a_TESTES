'''
Questão 6: Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média.
'''
max_lista = 20

def ler_lista(nome):
    l = []
    for i in range(max_lista):
        num = int(input(f"Digite  {nome} do produto {i+1}: "))
        l.append(num)
    return l

#Calculo do faturamento quantidade x preco
def cal_faturamento(qtd, preco):
    faturamentos = []
    for i in range(max_lista):
        faturamento = qtd[i] * preco[i]
        faturamentos.append(faturamento)
        
    return faturamentos

#Soma de todo o faturamento
def cal_total(faturamento):
    total = 0
    for valor in faturamento:
        total += valor
    return total

#Calculo da media do faturamento
def cal_media(faturamento):
    total = cal_total(faturamento)
    return total / max_lista

#Retornar o valor abaixo da media
def abaixo_da_media(faturamento, media):
    qtd = 0
    for valor in faturamento:
        if valor < media:
            qtd += 1
    return qtd

#Principal
print(f"-- Digite as quantidades dos {max_lista} produtos --")
quantidade = ler_lista("a quantidade")

print(f"\n-- Digite os precos dos {max_lista} produtos --")
precos = ler_lista("o preço")

faturamento = cal_faturamento(quantidade, precos)
print("\n--- Faturamento de cada produto ---")
for i in range(max_lista):
    print(f"Produto {i+1}: R$ {faturamento[i]:.2f}")
    
total = cal_total(faturamento)
media = cal_media(faturamento)
contar_baixo_media = abaixo_da_media(faturamento, media)

print(f"\nFaturamento total: R$ {total:.2f}")
print(f"Média dos faturamentos: R$ {media:.2f}")
print(f"Faturamentos abaixo da média: {contar_baixo_media}")