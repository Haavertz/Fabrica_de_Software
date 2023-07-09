#Leia três números e mostre o maior deles 1 forma

number1 = float(input("Qual o primeiro numero: "))
number2 = float(input("Qual o segundo numero: "))
number3 = float(input("Qual o terceiro numero: "))

lista = [number1,number2,number3]

print (max(lista))

print ()

#Leia três números e mostre o maior deles 2 forma

if (number1>number2 and number1 > number3):
    print (number1)
elif (number2>number1 and number1 > number3):
    print (number2)
elif (number3>number1 and number3>number2):
    print (number3)

#Leia três números e mostre o menor deles 

number1 = float(input("Qual o primeiro numero: "))
number2 = float(input("Qual o segundo numero: "))
number3 = float(input("Qual o terceiro numero: "))

lista = [number1,number2,number3]

print (min(lista))