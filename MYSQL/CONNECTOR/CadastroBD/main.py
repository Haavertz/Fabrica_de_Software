import os
from bd import MyBD

while True:
    print("-="*20)
    print("-=", "       BEM VINDO AO CADASTRO      ", "=-")
    print("-="*20)
    os.system("pause")
    os.system("cls")
    
    print("O QUE GOSTARIA DE FAZER? \n")
    print("1 > SE CADASTRAR")
    print("2 > PROCURAR CADASTRO")
    print("3 > EXCLUIR CADASTRO")
    print("4 > SAIR \n")
    
    escolha = int(input("ESCOLHA: "))
    
    if escolha == 1:
        os.system("cls")
        
        print("-="*20)
        print("-=", "       BEM VINDO AO CADASTRO       ", "=-")
        print("-="*20)
        
        os.system("pause")
        os.system("cls")
        
        nome = input("DIGITE SEU NOME: ")
        sobrenome = input("DIGITE SEU SOBRENOME: ")
        cpf = input("DIGITE SEU CPF: ")
        email = input("DIGITE SEU EMAIL: ")
        telefone = input("DIGITE SEU TELEFONE: ")
        endereco = input("DIGITE SEU ENDEREÇO: ")
        data_nascimento = input("DIGITE SUA DATA DE NASCIMENTO: ")
        complemento = input("DIGITE SEU COMPLEMENTO: ")
        cep = input("DIGITE SEU CEP: ")
        senha = input("DIGITE SUA SENHA: ")
        
        os.system("pause")
        os.system("cls")
                
        
        Banco = MyBD()      
        Banco.insert_values(nome, sobrenome, cpf, email, telefone, endereco, data_nascimento, complemento, cep, senha)
        
        continue
    
    if escolha == 2:
        os.system("cls")
        
        print("-="*20)
        print("-=", "       BEM VINDO AO PROCURAR       ", "=-")
        print("-="*20)
        
        os.system("pause")
        os.system("cls")
        
        numberID = int(input("DIGITE O ID DE QUEM PROCURA: "))
                
        os.system("pause")
        os.system("cls")
        
        Banco = MyBD()
        Banco.select_values(numberID)
                
        os.system("pause")
        os.system("cls")
        
    if escolha == 3:
        os.system("cls")
        
        print("-="*20)
        print("-=", "       BEM VINDO AO EXCLUIR       ", "=-")
        print("-="*20)
        
        os.system("pause")
        os.system("cls")
        
        numberID = int(input("DIGITE O ID DE QUEM DESEJA EXCLUIR: "))

        Banco = MyBD()
        Banco.exclude_values(numberID)
        
        os.system("pause")
        os.system("cls")
        
        continue
    
    if escolha == 4:
        break
    