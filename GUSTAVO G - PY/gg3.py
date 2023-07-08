from random import randint

def sorteio():
    valor1=0
    for valor1 in range(0,5):
        a = randint(0,100)
    print (a)


def somaPar(* num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += + valor
    print (soma)

somaPar(2,4,5,6,10)
sorteio()
