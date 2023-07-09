
def hello (nome): #(NOME) = Isto significa quê voce esta criando uma variavel onde vc vai chama depois, caso não chame irá dar erro.
    print ("Olá", nome) #O que tem 

nome = input("Qual seu nome: ")
hello (nome) #Aqui onde puxamos a variavel (aqui eu coloquei um input para o ser mais interativo para o usuario.)

def hello2 (nome2,idade): #Coloquei 2 variaveis consequentemente terei que puxar 2 variavel, senao, dará erro!
    print ("Olá,",nome2,"com", idade, "anos.")

hello2 ("Gleison", 17)

#    Exemplo1:

def calculator_pagamento(horas_trabalhadas, valor_hora):
    import os
    horas = float(horas_trabalhadas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_end = horas - 40
        salario = 40*taxa+(h_end*(1.5*taxa))
    print ("O pagamento será de: ", end="")
    print (salario)
    os.system("pause")
    os.system("cls")


hora2 = int(input("Colque as horas trabalhadas(H): "))
valor2 = int(input("Coloque o valor das Horas trabalhadas(V): "))

calculator_pagamento(hora2,valor2)

'''calculator_pagamento (60,4)'''

#    Exercicio2:

def soma(x,y):
    result = x + y
    return result #Retornar um valor, mostrando o valor e podendo fazer alteraçoes e manipulaçoes com ele
a=int(input("primeiro numero:"))
b=int(input("segundo numero:"))
res=soma(a,b)
print("soma:",res)

