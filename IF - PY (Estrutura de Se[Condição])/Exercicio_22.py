number1 = int(input("Qual o primeiro numero: "))
number2 = int(input("Qual o segundo numero: "))

number3 = (number1 + number2)/2

if number3 >= 7 and number3 <= 10:
    print ("aprovado")
elif number3 >= 5 and number3 < 6.99:
    print ("Recuperação")
else:
    print ("reprovado")
