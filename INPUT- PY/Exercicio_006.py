

nome = input("Nome é: ")
sal = float(input("Salario é: "))
print ("O funcionário %s recebeu %.2f" % (nome,sal))

'''nome = input("Nome é: ")
sal = (input("Salario é: "))
print ("O funcionário %s recebeu %.2f" % (nome,sal))'''
# Maneira errada, pois, se caso eu n declaro que o sal seja float ele irá ler como uma string e não irar adentrar dentro do (%.2f (sal))