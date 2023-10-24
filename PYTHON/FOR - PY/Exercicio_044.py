
valor = int(input("Digite a quantidade de item na sua compra: ")) 
fon = 0
for i in range(valor):
    preco = 0 + 1.99
    fon = fon + preco
    
    print (i+1, "- %.2f" %fon)
