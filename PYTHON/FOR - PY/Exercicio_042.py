lista = []
lista2 = []
item = 0
for j in range(5,0):
    lista.append(input("Digite um número inteiro: "))
    for item in lista:
        print (item*item)

for n in range(50,101,2):
    print(n)

for j in range(5):
    lista.append(input("Digite um número inteiro: "))
    print("Maior número: ", max(lista))
    print("Menor número: ", min(lista))