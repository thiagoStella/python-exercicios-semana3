'''Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes, removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos'''
frase = input("Digite um texto: ")
consoante = ""
for letra in frase:
    if letra.lower() not in "aeiou":
        consoante = consoante + letra
print(consoante)