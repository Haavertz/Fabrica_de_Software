
valor = int(input("Digite a quantidade de item na sua compra: ")) 
preco = 0
u = 0
i = 1
cont = 1
fon = 0
for i in range(valor):
    preco = u + 1.99
    fon = fon + preco
    print (cont, "- %.2f" %fon)
    cont = cont + 1
