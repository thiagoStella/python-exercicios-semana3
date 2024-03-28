'''Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final essas informações.'''
par = 0
impar = 0
for i in range(1,11):
    num = int(input("Digite o " +  str(i)  + "º numero: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1    
print("Contém", par, "números pares e", impar, "ímpares.")