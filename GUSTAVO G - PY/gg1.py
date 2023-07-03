import os


def contagem(inicio,fim,pulo):
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print (f"{cont}", end=" ")
            cont += pulo
        print (end="\n")
    else: 
        cont = inicio
        while cont>= fim:
            print (f"{cont}", end=" ")
            cont -= pulo


while True:
    print ("DIGITE UMA LETRA PARA SAIR!")
    try:
        a = int(input("Digite um numero para inicio: "))
        b = int(input("Digite um numero para inicio: "))
        c = int(input("Digite um numero para inicio: "))
        contagem(a,b,c)
        os.system("pause")
        os.system("cls")
    except:
        os.system("cls")
        print ("Obrigado por usar o sistema!")
        break
            
