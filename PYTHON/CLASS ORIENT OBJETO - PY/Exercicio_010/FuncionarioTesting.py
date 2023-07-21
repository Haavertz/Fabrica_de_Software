from Funcionario import *
import os
while True:
    print("-="* 21)
    print("-="* 2, "Bem vindo ao Sistema de Educacao", "-="* 2)
    print("-="* 21)
    os.system("pause")
    os.system("cls")
    print("Bom, temos algumas opcoes disponiveis")
    print("1 - Coodernador")
    print("2 - Aluno")
    print("3 - Professor")
    print("4 - Limpeza")
    escolha = input("Escolha: ")    
    if escolha == "1":
        print("Para se registrar como Coodenador de uma escola você ira precisar ", end="")
        print("dos seguintes dados: ")
        try:
            nome = input("* Nome: ")
            cpf = int(input("* CPF: "))
            fone = int(input("* Telefone: "))
            salario = int(input("* Salario: "))
        except:
            print("Valor Invalido!")
        else:   
            os.system("cls")
            c1 = Coodenador(nome,cpf,fone,salario)
        