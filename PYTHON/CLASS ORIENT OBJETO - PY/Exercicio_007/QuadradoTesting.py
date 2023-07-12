from Quadrado import *


while True:        
    valorQuadrado = float(input("Digite o valor do quadrado: "))
    print ("Gostaria de mudar o valor (1)(N/Q)?")
    print ("0 - Sair")
    escolha = int(input("Escolha: "))
    if escolha == 1:
         valorQuadrado = float(input("Digite o valor do quadrado: "))
         tamanho = Quadrado(valorQuadrado)
         tamanho.mostrarArea()
    if escolha == 0:
        break
    else:
        tamanho = Quadrado(valorQuadrado)
        tamanho.mostrarArea()
