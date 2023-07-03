import os

#Vai pega o maior numero e mostrar quantos numeros foram digitados

def maior (* num):
    cont = 0
    list1 = []
    for valor in num:
        cont += + 1
        list1.append(valor)
        print (valor)
    print (f"A quantidade de valores digitados foram de: {cont}")
    print ("O maior numero foi ", max(list1))


while True:
    print ("DIGITE UMA LETRA PARA SAIR!")
    try:
        a = int(input("Digite um numero para inicio: "))
        totaltly = maior (a)
    except:
        os.system("cls")
        print (totaltly)
        print ("Obrigado por usar o sistema!")
        break
            
