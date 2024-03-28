'''Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles.'''
menor = 0
maior = 0
for i in range(1,6):
    num = int(input("Digite o " + str(i) + "º numero: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("O menor número é:", menor, "e o maior é: ", maior)