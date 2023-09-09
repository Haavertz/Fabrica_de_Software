def tracos ():
    print ("="*30)


def calcularLargAltura (altura, largura):
    soma = altura * largura
    print ("Valor da altura A= %.2f e da Largura %.2f é de %.2f" %(altura,largura,soma)) 
    print (soma)

valor1 = float(input("Porfavor digite o valor da Altura (m): "))
valor2 = float(input("Porfavor digite o valor da Largura (m): "))
tracos()
calcularLargAltura(valor1,valor2)
'''totaly = calcularLargAltura(valor1,valor2)'''
