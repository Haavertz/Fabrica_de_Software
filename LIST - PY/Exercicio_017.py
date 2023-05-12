
#Del deletar <- literal

a = [ 'um','dois', 'tres']
del a[1]
print (a)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print (lista)

#Apennd 

b = 84
a = [81,82,83]
a.append(b) #Adicionar o numero dentro do append no final da lista
print (a)

#Sort ordena de forma crescente
#Reverse inverte a ordem da lista, mas nao a ordena.
#lista.sort (reverse=True) ordenar os valor de forma reversa
#index (print (a.index(4))) ele acha a posição do elemento - a primeira vez que ele aparecer
#Insert espreme e coloca o 100 na posição que a pessoa colocou
#Count (print (a.count)) quantas vezes vai aparecer determinada coisa

a = [1,2,5,4,7,6]
a.sort ()
print (a)

a = [1,2,5,4,7,6]
a.sort (reverse=True)
print (a)

a = [1,2,5,4,7,6]
a.reverse ()
print (a)

a = [1,2,5,4,7,6]
print (a.index(4))

a = [1,2,3,4,5,6]
a.insert (1,100)
print (a)

a = [1,2,3,4,5,6]

print (a.count (1))

a = [1,2,3,4,5,6]
a.pop (4) #Caso n tenha nada ele irar remover o ultimo
print (a)


