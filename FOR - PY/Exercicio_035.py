nomes = ["Leticia", "Joao", "Afonso"]
for n in nomes: #Entra e armazena dentro de n
    print (n)

ints = 1,101
for n in ints:
    print (n)

ints = "joao"
for n in ints:
    print (n)

nomes = ["Leticia", "Joao", "Afonso"] #Faço com que imprima até chegar no joao, depois disso é para parar.
for n in nomes:
    if n == "Joao":
        continue
    print (n)

for x in range(2, 10, 2): #Ranger percorre um conjuinto de codigo determinado numero de vezes, lembrando que ele conta (2,10,2) o primeiro 2 e onde deve iniciar o 10 e o 2 e o encremento, quanto ele vai pular
    print (x)

for x in range(100,0,-1): #Contar ao contrario
    print (x)