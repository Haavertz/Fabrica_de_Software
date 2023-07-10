from Conta import *


while True:
    print ("1 - Cadastro")
    print ("2 - Saque")
    print ("3 - Depositar")
    print ("4 - Extrato")
    escolha = input("Escolha: ")
    if escolha == "1":
        nome = input("Digite seu nome para cadastro: ")
        nomeconta = input("Digite o nome da conta: ")
        fone = int(input("Digite o seu telefone: "))
        saldo = int(input("Digite o seu saldo: "))
        cpf = int(input("Digite o seu CPF: "))
        agencia = int(input("Digite a agencia: "))
        c1 = Conta(nome,nomeconta,fone,saldo,cpf,agencia)
    elif escolha == "2":
        saque1 = int(input("Digite o valor do saque"))
        c1.saque(saque1)
    elif escolha == "3":
        deposit = int(input("Valor depositado: "))
        c1.depositar(deposit)
    elif escolha == "4":
        print ("O extrato disto é: ")
        c1.extrato()
    else:
        print ("Vai toma no seu cu(zoera)")
        break




