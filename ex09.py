'''Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio), 
seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo). 
Ao incluir um produto, deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. Todos os dados devem ser validados. 
Ao final da compra, deve ser informado o valor total do pedido.'''

print(":::::::::::  SISTEMA DE VENDAS :::::::::::::: \n")
vendas = 0
continuar = True
while continuar:
    while True:
        prod = str(input("Digite o nome do produto: "))
        if prod != '':
            break
        else:
            print("por favor, digite o produto desejado!")
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
            if valor <= 0:
                print("Digite um valor em dinheiro!")
            else:
                break
        except ValueError:
            print("Valor do produto inválido.")
    while True:
        try:
            quantidade = int(input("Digite a quantidade a ser adquirida: "))
            if quantidade < 1:
                print("valor inválido!")
            else:
                break
        except ValueError:
            print("Valor do produto inválido.")

    vendas += valor * quantidade

    resposta = input("Produto inserido no carrinho. Deseja continuar comprando? ( S / N )")
    carrinho = resposta.lower()
    if carrinho == "n":
        continuar = False
print(f"Valor total: R$ {vendas:.2f}")





'''
        print("por favor, digite o produto desejado!")
    valor = float(input("Digite o valor do produto: "))
    if valor <= 0:
        print("Digite um valor em dinheiro!")
    quantidade = int(input("Digite a quantidade a ser adquirida: "))
    if quantidade < 1:
        print("valor inválido!")
    vendas = valor * quantidade
    break
opcao = input("Deseja fazer mais compras? ZERO para finalizar")

print("A sua compra deu: R$", vendas)

'''


