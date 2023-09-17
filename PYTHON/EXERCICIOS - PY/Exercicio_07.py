
# Faça um Programa que leia um nome de usuario e a sua senha e não
# aceite a senha igual ao nome do usuario, mostrando uma mensagem de erro e voltando a pedir as informacoes

while True:
    
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    
    if senha != nome:
        print("Cadastrado com Sucesso")
        break
    else:
        print("Senha invalida!")
        continue