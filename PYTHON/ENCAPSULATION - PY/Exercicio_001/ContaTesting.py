from Conta import *

c1 = Conta("Gleison",1, 1200, "gleison", 20)

c1.depositar(20)
c1.sacar("gleison")
senha = input("Digite a senha correta (gleison): ")
c1.sacar(senha)
print (c1.senha)