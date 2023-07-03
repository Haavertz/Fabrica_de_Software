#Nome personalizado
a = "1"
def escreva(msg):
    tiozin = len(msg) + 4
    print ("-" * tiozin)
    print (f"  {msg}")
    print ("-" * tiozin)


while a != "0":
    a = input("Digite um nome (0 para parar): ")
    escreva(a) 

