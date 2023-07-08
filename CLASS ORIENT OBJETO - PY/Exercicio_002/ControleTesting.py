from Controle import *
while True:
        
    print ("Digite o botão: ")
    print ("1 - Mutado")
    print ("2 - Desligado")
    print ("3 - Aumenta Volumu ")
    print ("4 - DIminuir Volumu ")
    print ("0 - sair ")
    try:
        escolha = int(input("Escolha: "))
        escolha2 = Controle(escolha)
    except:
        print("Valor invalido")
    else:
        if escolha == 1:
            escolha2.muto()
        elif escolha == 2:
            escolha2.desligado()
        elif escolha == 3:
            escolha2.aumentaVolume()
        elif escolha == 4:
            escolha2.diminuirVolume()
        elif escolha == 0:
            break