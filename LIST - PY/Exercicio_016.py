
#MIN = menor elemento
#MAX = maior elemento
#SUM = somar os elementos

a = [1,2,3,4,5,6,7,8,9,10]
print (min(a))
print (max(a))
print (sum(a))

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print (lista [1:3])
print (lista [:4])
print (lista [3:])
print (lista [:])
print (lista [0:6])

#Com isto eu consigo alterar strings dentro da lista, difentemente da string normal.

frutas = ["banana", "maça", "cereja"]
print (frutas)
frutas [0] = "pera"
frutas [-1] = "laranja"
print (frutas)

#Substituir o casa por escola exercicio:

lista = ["flor", "azul", [1,"casa"]]
print (lista)
lista [2][1] = "escola" #entrar na lista1, contar o "flor" como 0 e "azul" como 1, depois contar o (1) como 0 e o "casa" como 1
print (lista)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print (lista)
lista [1:3] = ['x', 'y'] #mudar o B e o C para X e Y
print (lista)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print (lista)
print (len(lista))
lista [1:3] = [] #Eliminar um elemento de uma lista
print (lista)
print (len(lista))

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print (lista)
print (len(lista))
lista [1:1] = ['x'] #Desta forma ele irá Adicionar atrâs do B por X 
print (lista)
print (len(lista))

lista = [4,2,8,6,5]
lista[2] = [True]
print (lista)