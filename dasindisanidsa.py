'''from getpass import getpass
import calendar '''
import secrets
'''yy = int (input("Informe o ano: "))
mm = int (input("Informe o mes: "))

print ("Calewndario de: \n", calendar. month(yy,mm))'''


'''senha = getpass("DIgite sua senha: ")
confirmSenha = getpass("Confime a senha: ")

if senha == confirmSenha:
    print ("Senha correta!")
else:
    print ("Senha incorreta!")'''

sorteio = []
sorteio2 = []
while sorteio != "0":
    sorteio = input("Digite o nome: ")
    if sorteio == '0':
        break
    sorteio2.append(sorteio)
print (secrets.choice(sorteio2))
