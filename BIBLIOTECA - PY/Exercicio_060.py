import math 
import datetime as dt
import time as tm
import secrets as sc

'''print (math.ceil(15.4)) #Retorna o numero sempre pra cima ex: 15.5 vai pra 16 ou 15.2 vai pra 16 sempre pra cima
print (math.floor(3.7)) #Retorna o numero sempre pra baixo ex: 15.7 vai pra 15 ou 15.2 vai pra 15 sempre pra baixo
print (math.fabs(-11.7)) #Retorna um valor absoluto 
print (math.factorial(5)) #Retorna um valor fatorial
print (math.isqrt(49)) #Retorna a raiz quadrada do numero informado (Inteiro)
print (math.sqrt(50)) #Retorna a raiz quadrada porém em float
print (math.pow(2,10)) #Retorna o valor elevado ao quadrado


print (dt.date.today()) #Retorna a data
print (dt.date.today().strftime("%d/%m/%y")) #Retorna a data modificada ("/")
print (dt.datetime.now()) #Retorna com o horario
print (dt.datetime.now().strftime("%d/%m/%y %h:%m%"))
#WHILE para testa a data
while True:
    print (dt.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
#===================================
#Serve para testa a velocidade do pc 
a=0
x = tm.perf_counter()
while a < 10000:
    print (a)
    a +=1

y = tm.perf_counter()
print (y-x)
print (tm.perf_counter())
#===================================

random = sc.randbelow(100) #Gera uma senha aleatoria
print (random)

print (sc.randbelow(100))
random = sc.choice([1,2,3,4,5,6,7,8,9,10])
print (random)

random = sc.randbits(10)'''
random = sc.randbits(100)

print (random)

random = sc.token_bytes(16)
print  (random)
print ("Retorna uma string de byte aleatória contendo nbytes número de bytes.")

random = sc.token_hex(12)
print (random)