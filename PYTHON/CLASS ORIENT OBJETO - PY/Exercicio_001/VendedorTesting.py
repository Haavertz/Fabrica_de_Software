from Vendedor import *


vendedor1 = Vendedor("Gleison",90)
print (vendedor1.nome)
##############################################################################

a = input("Nome: ")
b = int(input("Valor: "))

vendedor2 = Vendedor(a,b)
print (vendedor2.nome)
print (vendedor2.vendas)

##############################################################################
vendedor3 = Vendedor("",300) #Tem que colocar 2 parametros e não (vendedor3 = Vendedor(30))
vendedor3.bateu_meta(100)