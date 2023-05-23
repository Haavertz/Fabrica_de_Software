
#Verifique se três números podem formar um triângulo retângulo.

print ("="* 38, "Bem-Vindo a Verificação do Triangulo Retangulo", "=" * 38)
number1 = float(input("Digite o primeiro numero: ")) #Pedir o numero para vermos se eles irão se torna um Triangulo Retangulo
number2 = float(input("Digite o segundo numero: "))
number3 = float(input("Digite o terceiro numero: "))

if number1 > number2 and number1 > number3: #Precisamos testa se o primeiro numero digitado é maior que os outros para entrar nessa condição
    hip = number1 #Caso entre nesta condição ele irão entrar dentro da variavel HIP
    if hip**2 == number2**2 + number3**2: #Entrando nessa condição utilizaremos Pitágoras para testarmos se os numeros digitados irão ser um triangulo (com o simbolo da == para testar se a hipotenusa é igual aos catetos)
        print ("\nÉ um triangulo retangulo!") #Caso seja verdade ele irá imprimir isto
    else: #Caso seja falso ele irá entrar neste ELSE para informar que o numero digitado não é um Triangulo Retangulo
        print ("\nNÃO é um triangulo retangulo")
if number2 > number1 and number2 > number3:
    hip = number2
    if hip**2 == number1**2 + number3**2:
        print ("\nÉ um triangulo retangulo!")
    else:
        print ("\nNÃO é um triangulo retangulo")
if number3 > number1 and number3 > number2:
    hip = number3
    if hip**2 == number2**2 + number1**2:
        print ("\nÉ um Triangulo Retangulo!")
    else:
        print ("\nNÃO é um Triangulo Retangulo")

