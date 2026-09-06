'''
Questão 11: Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
==== =MENU========
1)Cadastar nome
2)Pesquisar nome
3)Listar todos os nome
0) Sair do programa
——————–
Digite sua escolha:_
'''

lista = []

quantidade = int(input("Digite a quantidade de posições que deseja: "))

def cadastrar():
    if len(lista) < quantidade:
        for i in range(quantidade):
            nome = input(f"Digite {i+1}º nome: ")
            lista.append(nome)
            
        return "Nome Cadastrado!!"
    
    else:
        return "A lista ta cheia!"
    
def pesquisar():
    nome = input("Digite o nome que deseja pesquisar: ")
    
    encontrado = False
                
    for pessoa in lista:
        if pessoa == nome:
            encontrado = True
                    
    if encontrado:
        return "Nome encontrado!"
    else:
        return "Nome não encontrado!"
    
    
def listar():
    return lista

#PRINCIPAL
opcao = -1
while opcao !=0:
    print(''' \n======= MENU =======
1) Cadastrar Nome
2) Pesquisar Nome
3) Listar todos os nomes
0) Sair
''')
    
    opcao = int(input("Digite sua escolha: "))
        
#opções
    if opcao == 1: #cadastrar
        print("\n",cadastrar())
                           
    elif opcao == 2: #Pesquisar nome
        print("\n",pesquisar())
                
    elif opcao == 3: #Listar os nomes
        print("\n",listar())

    elif opcao == 0: #Encerrar
        print("\nPrograma encerrado.")
            
    else:
            print("\nOpção invalida!")