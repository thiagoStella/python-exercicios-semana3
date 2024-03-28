'''Crie um programa que peça para o usuário inserir um login e uma senha. 
Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações. 
Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".'''
while True:
    login = str(input("Digite seu login: "))
    senha = str(input("Digite a senha: "))
    if login == senha:
        print("O nome de usuários e senha devem ser diferentes!")
    else:
        break
print("Bem vindo ao sistema...")


