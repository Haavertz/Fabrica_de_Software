lista = []
lista2 = []

for j in range(10):
    n = int(input("Digite um número inteiro: "))
    if n > 0:
        
        lista.append(n)
    elif n < 0:
        lista2.append(n)
print("Número positivos: ", len(lista))
for itens in lista:
    print(itens, end=", ")
print("\nNúmero negativos: ", len(lista2))
for itens in lista2:
    print(itens, end=", ")