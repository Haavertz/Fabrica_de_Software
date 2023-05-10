#Aréa de um circulo, calcule e mostre sua área.

raio = float(input("Qual o raio do círculo: "))
area = raio**2*3.14159265359
print(area)

#Calcular a area de um quadrado, mostrar o dobro dessa area

quadrado1 = int(input("Qual o lado do quadrado: "))
print ("Valor normal:",quadrado1**2)
print ("Valor multiplicado:", quadrado1**2*2)

#Salario por horas trabalhadas no mes.

salario = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalha por mês? "))
result = salario*horas
print ("O valor que você ganha por horas é %.2f e a quantidade de horas é %.2f por fim o valor em quatro casas descimais são %.2f" % (salario,horas,result))

#Pedir 2 numeros inteiros e um numero real.

real1 = float(input("Me diga um numero real: "))
int1 = int(input("Me diga um numero inteiro: "))
int2 = int(input("Me diga um numero inteiro: "))

print ("O valor real é %f e os inteiro são %d e %d." % (real1,int1,int2))
