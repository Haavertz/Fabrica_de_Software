import os

cont = 0 
cont2 = 0
cont3 = 0
cont4 = 0
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
                cont = cont + 1
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
                duracao = int(input("Duração da sua viagem: "))
                valorPassagem = float(input("Digite o valor da passagem: "))
                cont2 = cont2 + 1
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
                qntPassageiros = int(input("Quantidade de Passageiros: "))
                cont3 = cont3 + 1
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
                cont4 = cont4 + 1
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
                if cont > 0:
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
                        os.system("pause")
                        os.system("cls")
                        print ("Este dado não esta cadastrado. Tente novamente.")
                    except:
                        print ("ERRO")
                else:
                     print ("Não temos esses dados")
                     os.system("pause")
                     os.system("cls")
            elif escolha2 == 2:
                if cont2 > 0:
                    try:
                        print ("="*20)
                        print (destino)
                        print (origem)
                        print (duracao)
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
                        os.system("pause")
                        os.system("cls")
                        print ("Este dado não esta cadastrado. Tente novamente.")
                    except:
                        print ("ERRO")
                else:
                     print ("Nao temos esses dados")
                     os.system("pause")
                     os.system("cls")
            elif escolha2 == 3:
                if cont3 > 0: 
                    try:
                        print ("="*20)
                        print (modelo)
                        print (ano)
                        print (horasDeVoou)
                        print (cor)
                        print (qntPassageiros)
                        print ("="*20)
                        os.system("pause")
                        os.system("cls")
                    except ValueError:
                        print ("Este dado não esta cadastrado. Tente novamente.")
                        os.system("pause")
                        os.system("cls")
                        continue
                    except NameError:
                        os.system("pause")
                        os.system("cls")
                        print ("Este dado não esta cadastrado. Tente novamente.")
                else:
                    print ("Não temos esses dados!")
                    os.system("pause")
                    os.system("cls")
            elif escolha2 == 4:
                if cont4 > 0:          
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
                else:
                    print ("Não temos esses dados")
                    os.system("pause")
                    os.system("cls")
            if escolha2 == 5:
                try:
                    print ("===============")
                    print (nome)
                    print (sobrenome)
                    print (rg)
                    print (cpf)
                    print ("===============")
                    print (destino)
                    print (origem)
                    print (duracao)
                    print (valorPassagem, " Com desconto = ", valorComDesconto)
                    print ("===============")
                    print (modelo)
                    print (ano)
                    print (horasDeVoou)
                    print (cor)
                    print (qntPassageiros)
                    print ("===============")
                    print (nomeTripulação)
                    print (cargo)
                    print (idadeTripulação)
                    print (dataDeAdmissão)
                    print (fone)
                    print ("===============")
                    os.system("pause")
                    os.system("cls")
                except:
                    print ("Algum dos valores estão faltando")
                    os.system("pause")
                    os.system("cls")



    
        
    
          
          
