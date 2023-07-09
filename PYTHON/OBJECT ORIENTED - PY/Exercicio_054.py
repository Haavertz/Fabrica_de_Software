def inverte(nome,sobrenome):
    nomeIvers = sobrenome+" "+nome
    return nomeIvers

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
invertido = inverte(nome,sobrenome)
print ("Olá,",invertido)

def par(x):
    if (x%2)==0:
        return True
    else:
        return False
    
'''while True:
    try:  
        num = int(input("Insira um número: "))
        if par(num):
            print ("É par")
        else:
            print ("É impar")
    except:
        print ("Tente novamente!")
        continue
'''

def cadastro():
    name = input("Qual seu nome: ")
    age = input("Idade: ")
    return name,age
    
print ("Iniciando Cadastro...")
nome,idade=cadastro()
print ("Seu nome é",nome, "sua idade é", idade)
print ("Cadastro Concluido...")