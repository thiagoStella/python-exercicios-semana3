'''Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10'''
num = int(input("Digite qual o nome da tabuada: "))

for i in range(1,11):
    print(num, "x ", i, " = ", i * num)
    