from getpass import getpass #Deixa a senha invisivel

__cont = ["Login", "Gleison", "Mauricio"]
__senha = ["123","456", "789"]

while True:    
    
    cont_login = input("Digite seu login: ")
    senha_login = getpass("Digite sua senha: ")

    try:
        for i in __cont:
            if i == cont_login:
                cont_final = i

        for j in __senha:
            if j == senha_login:
                senha_final = j
            cont_index = __cont.index(cont_final)
            senha_index = __senha.index(senha_final)

        if cont_index == senha_index:
            print("Login Efetuado com sucesso!")
            break

    except:
        print("Não existe este cadastro no banco de dados!")

        
        