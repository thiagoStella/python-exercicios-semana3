'''Crie um programa que solicite ao usuário vários números e, ao digitar 0, calcule a média dos números informados.'''
soma = 0
media = 0
i = 0
while True:
    num = int(input("Digite os números para inserir na conta da média e ZERO para sair: \n"))
    i += 1
    if num == 0:
        break
    soma += num
    media = soma / i
print("A média dos números informados é: ", media)