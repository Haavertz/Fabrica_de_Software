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
                os.system("pause")
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
                print ("Calculando 5% de desconto...")
                os.system("pause")
                valorComDesconto = valorPassagem - (valorPassagem*0.05)
                print ("="*20)
                print ("Valor ficou:", valorComDesconto)  
                print ("="*20)          
                os.system("pause")
                os.system("cls")
                break
    elif escolha == 3:
        while True:
            try:
                modelo = input("Modelo do avião: ")
                ano = input("Digite o ano do avião: ")
                horasDeVoou = int(input("Digite a quantidade de horas de voou: "))
                cor = input("Digite a cor do avião: ")
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
        while True:
            os.system("cls")
            print ("1 - Relatorio do Cliente")
            print ("2 - Relatorio da Passagem")
            print ("3 - Relatorio do Avião")
            print ("4 - Relatorio da Tripulação")
            print ("5 - Relatorio TODOS!")
            escolha2 = int(input("ESCOLHA: "))
            if escolha2 == 1:
                try:
                    print ("="*20)
                    print (nome)
                    print (sobrenome)
                    print (rg)
                    print (cpf)
                    print ("="*20)
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
                    os.system("pause")
                    os.system("cls")
                    continue
                except NameError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
                except:
                    print ("ERRO")
            elif escolha2 == 2:
                try:
                    print ("="*20)
                    print (destino)
                    print (origem)
                    print (duração)
                    print (valorPassagem, " Com desconto = ", valorComDesconto)
                    print ("="*20)
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
                    os.system("pause")
                    os.system("cls")
                    continue
                except NameError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
                except:
                    print ("ERRO")
            elif escolha2 == 3:
                try:
                    print ("="*20)
                    print (modelo)
                    print (ano)
                    print (horasDeVoou)
                    print (cor)
                    print (QntPassageiros)
                    print ("="*20)
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
                    os.system("pause")
                    os.system("cls")
                    continue
                except NameError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
            elif escolha2 == 4:
                try:
                    print ("="*20)
                    print (nomeTripulação)
                    print (cargo)
                    print (idadeTripulação)
                    print (dataDeAdmissão)
                    print (fone)
                    print ("="*20)
                    os.system("pause")
                    os.system("cls")
                except ValueError:
                    print ("Este dado não esta cadastrado. Tente novamente.")
                    os.system("pause")
                    os.system("cls")
                    continue
                except:
                    print ("ERRO")
            elif escolha2 == 5:
                try:
                    print ("="*20)
                    print (nome)
                    print (sobrenome)
                    print (rg)
                    print (cpf)
                    print ("="*20)
                    print ("")
                    print ("="*20)
                    print (destino)
                    print (origem)
                    print (duração)
                    print (valorPassagem, " Com desconto = ", valorComDesconto)
                    print ("="*20)
                    print ("")
                    print ("="*20)
                    print (modelo)
                    print (ano)
                    print (horasDeVoou)
                    print (cor)
                    print (QntPassageiros)
                    print ("="*20)
                    print ("")
                    print ("="*20)
                    print (nomeTripulação)
                    print (cargo)
                    print (idadeTripulação)
                    print (dataDeAdmissão)
                    print (fone)
                    print ("="*20)
                except ValueError:
                    print ("Esta opção esta disponivel apenas se você fez todo o Cadastro!")
                    os.system("pause")
                    os.system("cls")
                    continue
                except:
                    print ("ERRO")



    
        
    
          
          
