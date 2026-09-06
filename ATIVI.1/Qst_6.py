'''Questão 6: 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.
'''

def poligonos(l, m):
    if l == 3:
        print("TRIANGULO")
        print(m * 3)
    
    elif l == 4:
        print("QUADRADO")
        print(m**2)
    
    elif l == 5:
        print("PENTAGONO") 
    
lados = int(input("Quantos lados tem o seu polígono: "))
medida = float(input("Digite a medida do lado: "))

poligonos(lados,medida)
    

