number1 = int(input("Qual o primeiro numero: "))
number2 = int(input("Qual o segundo numero: "))

number3 = (number1 + number2)/2

if (number3 >= 7 and number3<=10):
    print ("Aprovado", end="")
    if (number3 == 10 ):
        print (" Distinção")
elif (number3 < 7 and number3 > 0):
    print ("Reprovado")
