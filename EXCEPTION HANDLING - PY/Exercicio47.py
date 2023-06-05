import os
while True:
    try:
        print ("0 - Sair/Mostrar")
        print ("1 - Cadastro de Cliente")
        print ("2 - Cadastro de Passagem")
        print ("3 - Cadastro de Avião")
        print ("4 - Cadastro de Tripulação")
        escolha = int(input("Escolha: "))
    except ValueError:
        print ("Valor digitado não é um numero!")
        print ("Tente novamente...")
        os.system("pause")
        os.system("cls")
        continue
    except:
       print ("ERRO")
    if escolha == 1:
     while True:
        try:
            nome = input("Digite seu primeiro nome: ")
            sobrenome = input("Digite seu Sobrenome: ")
            rg = float(input("Digite seu RG: "))
            cpf = float(input("Digite seu CPF: "))
            os.system("pause")
            os.system("cls")
        except ValueError:
          print ("O quê você digitou não e valido, favor digitar um NUMERO!")
          os.system("cls")
          continue
        except:
         print ("ERRO")
        else:
           break
    elif escolha == 2:
       while True:
          try:
             destino = input("Digite seu Destino: ")
             origem = input("Digite sua origem: ")
             duração = int(input("Duração da sua viagem: "))
             valorPassagem = float(input("Digite o valor da passagem: "))
          except ValueError:
             print ("O quê você digitou não e valido, favor digitar um NUMERO!")
          except:
             print ("ERRO")
          else:
             print ("Calculando 5% /de desconto...")
             os.system("pause")
             valorComDesconto = (valorPassagem*0.05) - valorPassagem
             os.system("pause")
             os.system("cls")
             print ("Valor ficou: ", valorComDesconto)
             break
    elif escolha == 3:
       while True:
          try:
             modelo = input("Modelo do avião: ")
             ano = input("Digite o ano do avião: ")
             horasDeVoou = int(input("Digite a quantidade de horas "))
             cor = input("Digite a cor do avião")
             QntPassageiros = int(input("Quantidade de Passageiros: "))
          except ValueError:
             print ("O quê você digitou não e valido, favor digitar um NUMERO!")
          except:
             print ("ERRO")
          else:
             break
    elif escolha == 4:
       while True:
          try:
             nomeTripulação = input("Nome: ")
             cargo = input("Descrição do cargo: ")
             idadeTripulação = int(input("Idade da Tripulação: "))
             dataDeAdmissão = input("Data de Admissão")
             fone = int(input("Fone: "))
          except ValueError:
             print ("O quê você digitou não e valido, favor digitar um NUMERO!")
          except:
             print ("ERRO")
          else:
             break
    elif escolha == 0:
       try:
            print (nome)
            print (sobrenome)
            print (rg)
            print (cpf)
            print ("============")
            print (destino)
            print (origem)
            print (duração)
            print (valorPassagem, " Com desconto = ", valorComDesconto)
            print ("============")
            print (modelo)
            print (ano)
            print (horasDeVoou)
            print (cor)
            print (QntPassageiros)
            print ("============")
            print (nomeTripulação)
            print (cargo)
            print (idadeTripulação)
            print (dataDeAdmissão)
            print (fone)
       except:
          print ("FAÇA O CADASTRO PRIMEIRO...")
          os.system("pause")
          os.system("cls")
          continue

    
        
    
          
          
