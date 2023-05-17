
nome1 = input("Digite o nome do produto:")
nome2 = input("Digite o nome do 2 produto:")
nome3 = input("Digite o nome do 3 produto:")

number1 = float(input("Qual o valor do primeiro produto:"))
number2 = float(input("Qual o valor do segundo  produto: "))
number3 = float(input("Qual o valor do terceiro produto: "))

lista = [number1,number2,number3]

lista2 = min(lista)

if (lista2 == number1):
    print (nome1,number1)
elif (lista2 == number2):
    print (nome2,number2)
elif (lista2 == number3):
    print (nome3,number3)
    

