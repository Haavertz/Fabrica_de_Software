# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
# valor seja invalido e continue pedindo até que o usuário informe um valor válido

import os


a = 1
while a != 7:
    b = int(input("Digite um valor de 0 a 10: "))
    if b >= 0 and b <= 10:
        if b == 7:
            print("Valor correto!")
            a = b
        else:
            print("Valor invalido! Tente novamente...")
            os.system("pause")
            os.system("cls")
    else:
        print("Valor Fora do padrão de 0 a 10!")
        os.system("pause")
        os.system("cls")

        
