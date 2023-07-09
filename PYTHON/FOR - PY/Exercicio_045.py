menor = 9999999
maior = -1

for i in range(1,3):
    passeio=int(input("Numero de veiculos de passeio(em 1999): "))
    vitima=int(input("Numero de acidentes de transito com vitimas  "))
    if vitima > maior:
       maior = vitima
       cidadeMaior = i + 1
    if vitima < maior:
       cidadeMenor = i + 1
       menor = vitima
print (cidadeMaior)
#NÃO TERMINADO!