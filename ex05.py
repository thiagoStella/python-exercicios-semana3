'''Crie um programa que peça dois números ao usuário – o primeiro será o numerador e o segundo, o expoente. A saída do programa deve ser o resultado da operação: numerador elevado ao expoente. Observação: não use a função própria do Python que calcula automaticamente potência.'''
res =0
num = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))
for i in range(exp):
    res += num
print("O numero é: ", res)